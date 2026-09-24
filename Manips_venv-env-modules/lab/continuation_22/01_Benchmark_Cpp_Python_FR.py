#!/usr/bin/env python3
"""Standalone companion to slides 28–29; generated from the notebook cells.

Run: python 01_Benchmark_Cpp_Python_FR.py
Dependencies: numpy, pandas, matplotlib; an installed C++ compiler is optional.
Change size, warmups, repeats and run_cpp near the start of main().
Importing this file does not run the benchmark.
"""


def main():
    # # Même calcul, cinq chemins d'exécution
    #
    # **Compagnon autonome des slides 28–29 — Olivier Delrieu, 22 septembre 2026.**
    #
    # Convertir un million de valeurs de minutes en heures : `output = input / 60.0`.
    # Comparer une boucle **C++ compilée**, une **boucle Python**, **NumPy**,
    # **pandas vectorisé** et **pandas avec une lambda par valeur**.
    #
    # Les données et le programme C++ sont inclus. Ce carnet n'a besoin d'aucun
    # fichier du dépôt, d'aucune donnée téléchargée et d'aucun module enseignant.
    # Les durées sont recalculées sur votre machine : elles ne doivent pas
    # reproduire exactement les chiffres de la slide.
    #
    # **En local :** ouvrir ce fichier dans Jupyter ou VS Code et sélectionner le
    # noyau Python de votre environnement. Dépendances : `numpy`, `pandas` et
    # `matplotlib`. Si elles manquent, les installer dans cet environnement avec
    # `python -m pip install numpy pandas matplotlib`. Le script équivalent
    # `01_Benchmark_Cpp_Python_FR.py` s'exécute dans un terminal avec
    # `python 01_Benchmark_Cpp_Python_FR.py`. Le notebook nécessite aussi un noyau
    # Jupyter (par exemple `python -m pip install ipykernel`).
    #
    # **Dans Colab :** ouvrir <https://colab.research.google.com/>, choisir
    # **Fichier → Importer le notebook**, importer seulement ce `.ipynb`, puis
    # **Exécution → Tout exécuter** dans une session CPU. Aucun GPU n'est utile.
    # Si une dépendance manque, `%pip install numpy pandas matplotlib` peut être
    # exécuté dans une cellule séparée. Aucune installation n'est automatique.
    #
    # **C++ est facultatif :** le code cherche `g++`, puis `clang++`. Sans
    # compilateur disponible, ou si sa compilation/exécution échoue, les quatre
    # méthodes Python restent explorables. Les fichiers C++ temporaires sont
    # supprimés en fin d'exécution. Aucun fichier n'est écrit près du notebook.

    # ## 1. Paramètres et versions
    #
    # Les valeurs par défaut suivent le protocole de la slide : **1 000 000
    # valeurs, 3 échauffements, 11 mesures** par méthode. Commencer par prévoir
    # quels chemins appellent Python une fois par valeur. Pour une exploration
    # plus rapide, réduire `size`, puis rejouer toutes les cellules suivantes.

    import gc
    import json
    import math
    import os
    from pathlib import Path
    import platform
    import random
    import shutil
    import statistics
    import subprocess
    import tempfile
    from textwrap import dedent
    from time import perf_counter_ns

    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    size = 1_000_000
    warmups = 3
    repeats = 11
    run_cpp = True
    seed = 404

    if size < 1 or warmups < 1 or repeats < 1:
        raise ValueError("size, warmups and repeats must be positive integers.")

    print(platform.python_implementation(), platform.python_version())
    print("NumPy", np.__version__, "pandas", pd.__version__)
    print("Matplotlib", matplotlib.__version__)
    print(platform.system(), platform.machine(), "logical CPUs:", os.cpu_count())
    print(f"size={size:,}; warmups={warmups}; repeats={repeats}; seed={seed}")

    # ## 2. Les mêmes valeurs, trois représentations
    #
    # Une liste contient des objets Python `float`. NumPy stocke un tableau
    # homogène de `float64`. La Series pandas utilise ici ce tableau numérique
    # et lui associe un index. C++ utilisera des `double` contigus.
    #
    # Préparer et convertir les entrées **avant** de chronométrer. Les valeurs
    # sont finies, sans NA, et identiques dans toutes les représentations.

    values = (np.arange(size, dtype=np.int64) % 3600).astype(np.float64)
    list_values = values.tolist()
    series = pd.Series(values, copy=False)
    expected = np.array([value / 60.0 for value in list_values], dtype=np.float64)

    print("Input:", list_values[:5])
    print("Expected output:", expected[:5])
    print(type(list_values).__name__, type(list_values[0]).__name__)
    print(type(values).__name__, values.dtype)
    print(type(series).__name__, series.dtype)

    # ## 3. Quatre écritures en Python
    #
    # Les fonctions ci-dessous effectuent le même calcul et créent toutes une
    # nouvelle sortie. Les lambdas de `methods` lancent **un calcul complet**.
    # Celle passée à `Series.map` est appelée **pour chaque valeur**.
    #
    # NumPy et `series / 60.0` délèguent ici la boucle numérique à du code natif.
    # La présence de pandas ne garantit pas cette délégation : comparer ses
    # deux écritures avant de lancer le chronomètre.

    def python_loop(items):
        output = []
        for value in items:
            output.append(value / 60.0)
        return output

    methods = {
        "python_loop": lambda: python_loop(list_values),
        "numpy": lambda: values / 60.0,
        "pandas_vectorized": lambda: series / 60.0,
        "pandas_map_lambda": lambda: series.map(lambda value: value / 60.0),
    }

    def check(output):
        np.testing.assert_array_equal(np.asarray(output), expected)

    def summarize(samples):
        return {
            "median_ms": statistics.median(samples),
            "min_ms": min(samples),
            "max_ms": max(samples),
        }

    # ## 4. Échauffer, mesurer, puis vérifier chaque résultat
    #
    # **Dans le chronomètre :** allocation du résultat, calcul et construction
    # du conteneur de sortie. **Hors chronomètre :** préparation/conversion des
    # entrées, imports, vérification et suppression de la sortie, affichage.
    #
    # Chaque sortie est vérifiée, après chaque échauffement et chaque mesure.
    # L'ordre des quatre méthodes est mélangé à chaque tour avec `seed=404`.
    # Les listes et les tableaux n'ont pas la même représentation mémoire :
    # nous comparons des écritures usuelles, pas une division CPU isolée.
    #
    # `numexpr` est temporairement désactivé pour garder le chemin pandas/NumPy
    # décrit ici. Le ramasse-miettes cyclique de Python est suspendu pendant les
    # mesures. `finally` restaure ces deux réglages, même en cas d'erreur.
    # Aucune parallélisation explicite n'est demandée.

    timings = {name: [] for name in methods}
    gc_was_enabled = gc.isenabled()
    numexpr_was_enabled = pd.get_option("compute.use_numexpr")
    try:
        pd.set_option("compute.use_numexpr", False)
        gc.disable()
        for _ in range(warmups):
            for method in methods.values():
                output = method()
                check(output)
                del output

        ordering = list(methods)
        rng = random.Random(seed)
        for _ in range(repeats):
            rng.shuffle(ordering)
            for name in ordering:
                start = perf_counter_ns()
                output = methods[name]()
                end = perf_counter_ns()
                timings[name].append((end - start) / 1_000_000)
                check(output)
                del output
    finally:
        pd.set_option("compute.use_numexpr", numexpr_was_enabled)
        if gc_was_enabled:
            gc.enable()
        else:
            gc.disable()

    print(f"Four Python methods: {warmups} warmups and {repeats} measurements checked.")

    # ## 5. C++ facultatif : source complet, compilation puis mesure interne
    #
    # Lire surtout `divide` : il alloue une sortie et applique `input[i] / 60.0`.
    # `verify` lit et contrôle chaque résultat **après** l'arrêt du chronomètre.
    # Cette utilisation observable empêche de supprimer le calcul comme inutile.
    #
    # Le source est identique à celui utilisé pour la slide. Il est inclus dans
    # une chaîne de caractères Python pour que ce notebook reste autonome.
    # Les détails de compilation ne sont pas un prérequis pour l'atelier.

    cpp_source = dedent(r"""
    #include <chrono>
    #include <cmath>
    #include <cstddef>
    #include <cstdlib>
    #include <iomanip>
    #include <iostream>
    #include <memory>
    #include <stdexcept>
    #include <vector>

    // Allocate a new output and fill every element. No fast-math is used.
    __attribute__((noinline))
    std::unique_ptr<double[]> divide(const std::vector<double>& input) {
        auto output = std::unique_ptr<double[]>(new double[input.size()]);
        for (std::size_t i = 0; i < input.size(); ++i) {
            output[i] = input[i] / 60.0;
        }
        return output;
    }

    // Read every output outside the timer. Observable failures prevent the
    // compiler from deleting the timed computation as unused work.
    __attribute__((noinline))
    double verify(const double* output, const std::vector<double>& expected) {
        double checksum = 0.0;
        for (std::size_t i = 0; i < expected.size(); ++i) {
            if (output[i] != expected[i]) {
                throw std::runtime_error("Incorrect output");
            }
            checksum += output[i];
        }
        return checksum;
    }

    int main(int argc, char** argv) {
        if (argc != 4) {
            std::cerr << "Usage: divide SIZE WARMUPS REPEATS\n";
            return 2;
        }
        const auto size = static_cast<std::size_t>(std::stoull(argv[1]));
        const int warmups = std::stoi(argv[2]);
        const int repeats = std::stoi(argv[3]);
        if (size == 0 || warmups < 1 || repeats < 1) {
            return 2;
        }
        std::vector<double> input(size);
        std::vector<double> expected(size);
        for (std::size_t i = 0; i < size; ++i) {
            input[i] = static_cast<double>(i % 3600);
            expected[i] = input[i] / 60.0;
        }
        double checksum = 0.0;
        for (int i = 0; i < warmups; ++i) {
            const auto output = divide(input);
            checksum = verify(output.get(), expected);
        }
        std::vector<double> timings;
        timings.reserve(repeats);
        for (int i = 0; i < repeats; ++i) {
            const auto start = std::chrono::steady_clock::now();
            auto output = divide(input);
            const auto end = std::chrono::steady_clock::now();
            timings.push_back(std::chrono::duration<double, std::milli>(end - start).count());
            checksum = verify(output.get(), expected);
            // Output destruction follows verification, outside the measured interval.
        }
        std::cout << std::setprecision(17) << "{\"samples_ms\":[";
        for (std::size_t i = 0; i < timings.size(); ++i) {
            if (i) std::cout << ',';
            std::cout << timings[i];
        }
        std::cout << "],\"checksum\":" << checksum << ",\"correct\":true}\n";
    }
    """).lstrip("\n")

    # La compilation utilise `-O3 -std=c++17`, sans `-ffast-math` ni
    # `-march=native`. Son temps et celui du démarrage du programme ne sont pas
    # inclus : le programme C++ utilise son **propre chronomètre interne**.
    # Il exécute le même nombre d'échauffements et de mesures et contrôle tous
    # les éléments à chaque passage. C++ passe après les méthodes Python,
    # dans un processus séparé. Cela limite la portée d'un classement très fin.
    #
    # Si C++ est ignoré, le graphique n'affiche **aucune durée inventée** pour lui.
    # Le message donne la raison. Ne pas installer de compilateur pour poursuivre.

    compiler_flags = ["-O3", "-std=c++17"]
    timings.pop("cpp", None)
    compiler = shutil.which("g++") or shutil.which("clang++")
    cpp_status = "disabled: run_cpp is False"
    compiler_version = None
    native_result = None

    if run_cpp and compiler is None:
        cpp_status = "skipped: no g++ or clang++ compiler found"
    elif run_cpp:
        try:
            version = subprocess.run(
                [compiler, "--version"], capture_output=True, text=True,
                check=True, timeout=15,
            )
            compiler_version = version.stdout.splitlines()[0]
            with tempfile.TemporaryDirectory(prefix="python-course-benchmark-") as temp_dir:
                source_path = Path(temp_dir) / "divide.cpp"
                executable = Path(temp_dir) / ("divide.exe" if os.name == "nt" else "divide")
                source_path.write_text(cpp_source, encoding="utf-8")
                subprocess.run(
                    [compiler, *compiler_flags, str(source_path), "-o", str(executable)],
                    capture_output=True, text=True, check=True, timeout=120,
                )
                execution = subprocess.run(
                    [str(executable), str(size), str(warmups), str(repeats)],
                    capture_output=True, text=True, check=True, timeout=120,
                )
                native_result = json.loads(execution.stdout)
                samples = native_result["samples_ms"]
                if native_result["correct"] is not True or len(samples) != repeats:
                    raise ValueError("Unexpected C++ correctness report or number of samples.")
                if not all(isinstance(value, (int, float)) and math.isfinite(value)
                           and value > 0 for value in samples):
                    raise ValueError("Invalid C++ timing samples.")
            timings["cpp"] = samples
            cpp_status = "measured: all outputs checked in the C++ program"
        except (OSError, subprocess.SubprocessError, ValueError, KeyError, IndexError, TypeError) as error:
            native_result = None
            cpp_status = f"skipped: {type(error).__name__}: {error}"
            detail = getattr(error, "stderr", None)
            if detail:
                cpp_status += "\n" + str(detail).strip()[:1200]

    print("C++:", cpp_status)
    if compiler_version:
        print(compiler_version, " ".join(compiler_flags))

    # ## 6. Tableau et graphique : médiane, minimum et maximum
    #
    # Même ordre des méthodes que sur la slide. L'axe du temps est
    # **logarithmique** : une même distance représente un même facteur
    # multiplicatif. Le point indique la médiane ; le segment relie le minimum
    # au maximum des mesures. Ce segment **n'est pas un intervalle de confiance**.

    labels = {
        "cpp": "C++ : boucle compilée (-O3)",
        "python_loop": "Python : for + append",
        "pandas_vectorized": "pandas : Series / 60",
        "numpy": "NumPy : ndarray / 60",
        "pandas_map_lambda": "pandas : map(lambda)",
    }
    available = [name for name in labels if name in timings]
    results = pd.DataFrame([
        {"method": labels[name], **summarize(timings[name])}
        for name in available
    ]).set_index("method")
    print(results.to_string(float_format=lambda value: f"{value:.3f}"))

    fig, ax = plt.subplots(figsize=(11, 4.5))
    for position, name in enumerate(available):
        row = results.loc[labels[name]]
        color = "#B66B38" if name in {"python_loop", "pandas_map_lambda"} else "#23628C"
        ax.plot([row["min_ms"], row["max_ms"]], [position, position],
                color=color, linewidth=3)
        ax.scatter(row["median_ms"], position, color=color, s=65, zorder=3)
    ax.set_yticks(range(len(available)), [labels[name] for name in available])
    ax.invert_yaxis()
    ax.set_xscale("log")
    ax.set_xlabel("Durée en ms — axe logarithmique")
    ax.set_title(f"Même calcul : x / 60 — {size:,} valeurs".replace(",", " "))
    ax.grid(axis="x", which="both", alpha=0.2)
    ax.set_axisbelow(True)
    fig.tight_layout()
    plt.show()

    # ## 7. Explorer et interpréter
    #
    # 1. Pourquoi `series / 60.0` et `series.map(lambda value: value / 60.0)`
    #    n'ont-ils pas la même durée, alors qu'ils utilisent tous deux pandas ?
    # 2. Modifier `size` : `1_000`, `100_000`, puis `1_000_000`. Rejouer depuis
    #    les paramètres. Les coûts fixes et les plages min–max changent-ils ?
    # 3. Relancer sans modifier le code. Quels écarts persistent ? Quels écarts
    #    sont du même ordre que la variabilité entre mesures ?
    # 4. Que faudrait-il ajouter pour mesurer une analyse de bout en bout,
    #    incluant lecture CSV, conversion de types et export du résultat ?
    #
    # **Lecture attendue :** sur ce calcul numérique, NumPy et pandas vectorisé
    # peuvent atteindre le même ordre de grandeur que la boucle C++ compilée.
    # Une lambda n'accélère pas une opération à elle seule. Une opération pandas
    # sur du texte, des objets ou des NA peut emprunter un autre chemin.
    #
    # **Limites :** caches et allocateurs sont échauffés ; fréquence du CPU,
    # activité de fond et ressources partagées de Colab ne sont pas contrôlées.
    # Les versions, les conteneurs et la machine changent les résultats. Ce cas
    # ne mesure ni un temps complet d'analyse ni la rapidité générale d'un langage.


if __name__ == "__main__":
    main()
