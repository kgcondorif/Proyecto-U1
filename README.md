# Análisis Empírico y Comparativo de ShellSort y QuickSort

Repositorio oficial del proyecto de evaluación experimental y auditoría operacional de algoritmos de ordenamiento para la asignatura de Programación Avanzada (Semestre 2026-II) de la Escuela Profesional de Ingeniería de Sistemas e Informática (ESIS), Universidad Nacional Jorge Basadre Grohmann (UNJBG), Tacna, Perú.

---

## Descripción del proyecto

A pesar de que la teoría de complejidad asintótica establece cotas analíticas bien definidas para los algoritmos basados en comparaciones O(n log n) frente a O(n^2), el rendimiento real en plataformas modernas está fuertemente supeditado a factores microarquitectónicos como la localidad de referencia en la jerarquía de memoria caché ($L1/L2/L3$), la predicción de saltos y la gestión de la pila de llamadas.

Este proyecto implementa un banco de pruebas estricto y autocontenido en C++17 que audita el comportamiento empírico de ShellSort (algoritmo iterativo, *in-place*, basado en secuencias de incrementos decrecientes de Shell $k = \lfloor n/2 \rfloor$) y QuickSort (algoritmo recursivo basado en división y conquista optimizado con estrategia de pivote central).

El estudio analiza un espacio muestral de 1,500 ejecuciones controladas contemplando combinaciones de tres órdenes de magnitud de entrada ($n = 1\,000, 10\,000, 100\,000$), cinco patrones estocásticos de distribución de datos y 50 repeticiones independientes por escenario.

---

## Resultados clave y hallazgos empíricos

1. **Hegemonía de QuickSort en datos estocásticos (Caso promedio):**
   * En arreglos aleatorios de $n = 100\,000$ elementos, QuickSort superó a ShellSort en velocidad por un factor de $2.3\times$ (12.42 ms vs. 28.79 ms).
   * La selección del pivote central mantuvo la profundidad de la pila de llamadas acotada dentro de la cota logarítmica esperada ($\approx \log_2 n$).

2. **Degradación severa de QuickSort ante valores duplicados:**
   * Bajo el patrón de Duplicados Masivos ($n = 100\,000$), la variante estándar de QuickSort con pivote central sufrió una degradación operacional crítica, elevando su tiempo de ejecución a 285.51 ms y disparando el conteo de comparaciones a más de $2.13 \times 10^8$.
   * La asimetría en el particionamiento multiplicó la profundidad máxima de la pila de recursión por más de $20\times$ (alcanzando 6,150 niveles para $n = 100\,000$), representando un riesgo latente de desbordamiento de pila.

3. **Inmunidad y eficiencia de ShellSort en memoria caché:**
   * ShellSort demostró una notable estabilidad operacional en arreglos con alta presencia de duplicados (completando el ordenamiento de $n = 100\,000$ elementos en tan solo 11.87 ms).
   * En arreglos casi ordenados y preordenados, el esquema de pases por incrementos de ShellSort aprovecha la localidad espacial de la memoria caché del procesador, reduciendo los fallos de línea (*cache misses*) y realizando 0.00 intercambios físicos en entradas ascendentes.

---

## Matriz del diseño experimental

| Parámetro | Especificación Técnica |
| :--- | :--- |
| **Lenguaje y Estándar** | C++17 (compilado con la bandera de optimización `-O3`) |
| **Magnitudes de Entrada ($n$)** | $1\,000$, $10\,000$ y $100\,000$ enteros de 32 bits con signo (`int32_t`) |
| **Patrones (5)** | `Aleatorio` (uniforme), `Ascendente` (ordenado), `Descendente` (inverso), `Casi Ordenado` (5% de permutaciones) y `Duplicados` (alta densidad de claves idénticas) |
| **Generación Aleatoria** | Algoritmo Mersenne Twister (`std::mt19937`) con semillas estáticas fijas |
| **Semillas** | `1 - 50` (para garantizar reproducibilidad) |
| **Réplicas Estadísticas** | 50 corridas independientes por cada configuración ($3 \times 5 \times 50 = 1,500$ ejecuciones) |
| **Métricas Capturadas** | Tiempo (ms vía `std::chrono::high_resolution_clock`), comparaciones relacionales, intercambios y profundidad de pila |
| **Ultimo Commit hash** | (`8d2bdd5ca284519637932cd83d2ee04747745d6b`)

---

## Control del entorno e información de hardware

Para garantizar el aislamiento de variables de hardware, todas las mediciones de rendimiento se realizaron bajo las siguientes condiciones controladas:

* **Sistema Operativo:** Microsoft Windows 11 Home Single Language (Versión 26H2, Compilación de SO 26300.9711)[cite: 18]
* **Procesador (CPU):** Intel(R) Core(TM) 7 240H (2.50 GHz base, 10 núcleos, 16 procesadores lógicos)
* **Memoria RAM:** 16.0 GB DDR5 (SODIMM, velocidad de 5600 MT/s)
* **Compilador:** `g++.exe (MinGW-W64 x86_64-ucrt-posix-seh, built by Brecht Sanders, r8) 13.2.0`
* **Estándar de C++:** C++17
* **Generador Pseudoaleatorio:** `std::mt19937` con semillas controladas

---

## Resumen estadístico ($n = 100\,000$)

| Algoritmo | Patrón de Entrada | Tiempo Prom. (ms) | Mediana (ms) | Desv. Est. (ms) | Comparaciones Prom. | Intercambios Prom. | Profundidad Máx. Pila |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **QuickSort** | Aleatorio | **12.42** | 12.23 | 0.75 | $2.71 \times 10^6$ | $7.49 \times 10^5$ | 49 |
| **QuickSort** | Ascendente | **2.87** | 2.80 | 0.26 | $1.50 \times 10^6$ | $1.00 \times 10^5$ | 17 |
| **QuickSort** | Descendente | **3.31** | 3.22 | 0.34 | $1.63 \times 10^6$ | $2.10 \times 10^5$ | 17 |
| **QuickSort** | Casi Ordenado | **4.19** | 4.14 | 0.50 | $1.60 \times 10^6$ | $1.61 \times 10^5$ | 24 |
| **QuickSort** | Duplicados | **285.51** | 283.02 | 28.88 | $2.13 \times 10^8$ | $2.72 \times 10^5$ | 6,150 |
| **ShellSort** | Aleatorio | **28.79** | 28.65 | 1.24 | $4.34 \times 10^6$ | $3.66 \times 10^6$ | 0 (Iterativo) |
| **ShellSort** | Ascendente | **4.46** | 4.36 | 0.34 | $1.50 \times 10^6$ | 0.00 | 0 (Iterativo) |
| **ShellSort** | Descendente | **9.24** | 9.14 | 0.53 | $2.24 \times 10^6$ | $1.66 \times 10^6$ | 0 (Iterativo) |
| **ShellSort** | Casi Ordenado | **22.73** | 22.65 | 1.24 | $3.42 \times 10^6$ | $2.54 \times 10^6$ | 0 (Iterativo) |
| **ShellSort** | Duplicados | **11.87** | 11.65 | 1.08 | $2.02 \times 10^6$ | $8.31 \times 10^5$ | 0 (Iterativo) |

---

## Estructura del repositorio

```text
├── src/
│   ├── algoritmos.cpp        # Banco de pruebas experimental en C++
│   └── analisis.py           # Script automatizado de análisis estadístico y gráficos
├── results/                  # Archivos CSV generados y resultados analíticos
├── docs/                     # Artículo científico final
└── README.md                 # Documentación técnica y de reproducibilidad
```
---

## Instrucciones de reproducción y ejecución

### 1. Clonar el Repositorio
Para descargar el proyecto en tu máquina local, abre tu terminal y ejecuta:
```bash
git clone https://github.com/kgcondorif/Proyecto-U1.git
cd Proyecto-U1
```

### 2. Requisitos previos
* **Compilador de C++17:** Compatible con optimizaciones avanzadas (ej. `g++` vía MinGW-W64).
* **Python 3.x:** Con las librerías estadísticas y de visualización requeridas:
  ```bash
  pip install pandas matplotlib seaborn
  ```

### 3. Compilación y ejecución del banco de pruebas (C++)
Compila el código fuente en C++ utilizando la bandera de optimización máxima `-O3` para garantizar la fidelidad de las mediciones de hardware:

```bash
g++ -O3 src/algoritmos.cpp -o benchmark_sorting
./benchmark_sorting
```

### 4. Procesamiento estadístico y generación de gráficos (Python)
Una vez obtenido el archivo de datos crudos, ejecuta el script de análisis para calcular los estadísticos descriptivos (media, mediana, desviación estándar, mínimos y máximos) y exportar las figuras en alta resolución (300 DPI):

```bash
python src/analisis.py
```

* **Archivos generados en `results/`:**
  * `Resumen_tiempo.csv`, `Resumen_operaciones.csv`, `Resumen_100k.csv` y `Resumen_profundidad.csv`
  * `Quicksort_N_vs_Tiempo.png` (Fig. 1)
  * `Quicksort_N_vs_Comparaciones.png` (Fig. 2)
  * `Shellsort_N_vs_Tiempo.png` (Fig. 3)
  * `Shellsort_N_vs_Comparaciones.png` (Fig. 4)
  * `Rendimiento_comparativa.png` (Fig. 5)

---

## Autor

**Universidad Nacional Jorge Basadre Grohmann (UNJBG)**  
*Facultad de Ingeniería — Escuela Profesional de Ingeniería de Sistemas e Informática (ESIS)*  
Tacna, Perú.

* **Kael Gonzalo Condori Fora** (Código: 2026-119003) — *Correo:* [kgcondorif@unjbg.edu.pe](mailto:kgcondorif@unjbg.edu.pe)

---

## Video de exposición

**Video de Youtube**

Link: [https://youtu.be/tedNgr1efP8](https://youtu.be/tedNgr1efP8)