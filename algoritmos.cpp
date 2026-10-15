#include <iostream>
#include <vector>

using namespace std;

struct Contadores {
    long comparaciones;
    long intercambios;
    long profundidad;
};

void shellSort(vector<int> &v, Contadores &c);
void quickSort(vector<int> &v, int inicio, int fin, Contadores &c, int profundidad);

int main(){
    vector<int> a1, a2;
    Contadores c1 = {0, 0, 0};
    Contadores c2 = {0, 0, 0};
    int n;

    cin >> n;
    a1.resize(n);
    a2.resize(n);
    for (int i = 0; i < n; i++){
        cin >> a1[i];
        a2[i] = a1[i];
    }

    cout << "Vector original: ";
    for (int i = 0; i < n; i++){
        cout << a1[i] << " ";
    }
    cout << endl;
    
    shellSort(a1, c1);
    quickSort(a2, 0, n - 1, c2, 1);

    cout << "Vector ordenado con ShellSort: ";
    for (int i = 0; i < n; i++){
        cout << a1[i] << " ";
    }
    cout << endl;
    cout << "Metricas de ShellSort: " << endl;
    cout << "Comparaciones: " << c1.comparaciones << endl;
    cout << "Intercambios: " << c1.intercambios << endl;

    cout << "Vector ordenado con QuickSort: ";
    for (int i = 0; i < n; i++){
        cout << a2[i] << " ";
    }
    cout << endl;
    cout << "Metricas de QuickSort: " << endl;
    cout << "Comparaciones: " << c2.comparaciones << endl;
    cout << "Intercambios: " << c2.intercambios << endl;
    cout << "Profundidad de recursion: " << c2.profundidad << endl;

    return 0;
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