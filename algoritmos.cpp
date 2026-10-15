#include <iostream>
#include <vector>
#include <chrono>
#include <random>

using namespace std;

struct Contadores {
    long comparaciones;
    long intercambios;
    long profundidad;
    double tiempo;
};

vector<int> VectorAleatorio(int n, int patron, int semilla);
void shellSort(vector<int> &v, Contadores &c);
void quickSort(vector<int> &v, int inicio, int fin, Contadores &c, int profundidad);

int main(){
    vector<int> a1, a2;
    Contadores c1 = {0, 0, 0, 0};
    Contadores c2 = {0, 0, 0, 0};
    int n, patron, semilla;

    cin >> n >> patron >> semilla;

    a1 = VectorAleatorio(n, patron, semilla);
    a2 = a1;

    cout << "Vector original: ";
    for (int i = 0; i < n; i++){
        cout << a1[i] << " ";
    }
    cout << endl;
    
    auto inicio = chrono::high_resolution_clock::now();
    shellSort(a1, c1);
    auto final = chrono::high_resolution_clock::now();
    c1.tiempo = chrono::duration<double, milli>(final - inicio).count();

    auto inicio2 = chrono::high_resolution_clock::now();
    quickSort(a2, 0, n - 1, c2, 1);
    auto final2 = chrono::high_resolution_clock::now();
    c2.tiempo = chrono::duration<double, milli>(final2 - inicio2).count();

    cout << "Vector ordenado con ShellSort: ";
    for (int i = 0; i < n; i++){
        cout << a1[i] << " ";
    }
    cout << endl;
    cout << "Metricas de ShellSort: " << endl;
    cout << "Tiempo: " << c1.tiempo << " ms" << endl;
    cout << "Comparaciones: " << c1.comparaciones << endl;
    cout << "Intercambios: " << c1.intercambios << endl;

    cout << "Vector ordenado con QuickSort: ";
    for (int i = 0; i < n; i++){
        cout << a2[i] << " ";
    }
    cout << endl;
    cout << "Metricas de QuickSort: " << endl;
    cout << "Tiempo: " << c2.tiempo << " ms" << endl;
    cout << "Comparaciones: " << c2.comparaciones << endl;
    cout << "Intercambios: " << c2.intercambios << endl;
    cout << "Profundidad maxima de recursion: " << c2.profundidad << endl;

    return 0;
}

vector<int> VectorAleatorio(int n, int patron, int semilla){
    vector<int> v(n);
    mt19937 rng(semilla);

    if (patron == 1){
        uniform_int_distribution<int> dist(1, n * 10);
        for (int i = 0; i < n; i++){
            v[i] = dist(rng);
        }
    } 
    else if (patron == 2){
        for (int i = 0; i < n; i++){
            v[i] = i + 1;
        }
    } 
    else if (patron == 3){
        for (int i = 0; i < n; i++){
            v[i] = n - i;
        }
    } 
    else if (patron == 4){
        for (int i = 0; i < n; i++){
            v[i] = i + 1;
        }
        int permutaciones = max(1, static_cast<int>(n * 0.05));
        uniform_int_distribution<int> dist(0, n - 1);
        for (int i = 0; i < permutaciones; i++) {
            int idx1 = dist(rng);
            int idx2 = dist(rng);
            int aux = v[idx1];
            v[idx1] = v[idx2];
            v[idx2] = aux;
        }
    } 
    else if (patron == 5){
        uniform_int_distribution<int> dist(1, 20);
        for (int i = 0; i < n; i++){
            v[i] = dist(rng);
        }
    }

    return v;
}

void shellSort(vector<int> &v, Contadores &c){
    int n = v.size();
    int k, aux;
    k = (n + 1) / 2;
    
    while (k >= 1) {
        for (int i = 0; i + k < n; i++){
            aux = v[i + k];
            int j = i;

            while (j >= 0){
                c.comparaciones++;
                if (aux < v[j]){
                    j -= k;
                } 
                else {
                    break;
                }
            
            }

            for (int h = i + k; h > j + k; h -= k){
                v[h] = v[h - k];
                c.intercambios++;
            }
            if (j != i) {
                v[j + k] = aux;
                c.intercambios++;
            }
        }
        k /= 2;
    }
}

void quickSort(vector<int> &v, int inicio, int fin, Contadores &c, int profundidad){
    if (inicio >= fin){
        return;
    }

    if (profundidad > c.profundidad) {
        c.profundidad = profundidad;
    }

    int k = inicio;
    int izq = inicio;
    int der = fin;
    int pivote = v[inicio];

    while (izq < der) {
        for (der; der > izq; der--) {
            c.comparaciones++;
            if (v[der] < pivote) {
                v[k] = v[der];
                v[der] = pivote;
                k = der;
                c.intercambios++;
                break;
            }
        }

        for (izq; izq < der; izq++) {
            c.comparaciones++;
            if (v[izq] > pivote) {
                v[k] = v[izq];
                v[izq] = pivote;
                k = izq;
                c.intercambios++;
                break;
            }
        }
    }

    quickSort(v, inicio, k - 1, c, profundidad + 1);
    quickSort(v, k + 1, fin, c, profundidad + 1);
}