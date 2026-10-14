#include <iostream>
#include <vector>

using namespace std;

void shellSort(vector<int> &v);
void quickSort(vector<int> &v, int inicio, int fin);

int main(){
    vector<int> a1, a2;
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
    
    shellSort(a1);
    quickSort(a2, 0, n - 1);

    cout << "Vector ordenado con ShellSort: ";
    for (int i = 0; i < n; i++){
        cout << a1[i] << " ";
    }
    cout << endl;
    
    cout << "Vector ordenado con QuickSort: ";
    for (int i = 0; i < n; i++){
        cout << a2[i] << " ";
    }
    cout << endl;

    return 0;
}

void shellSort(vector<int> &v){
    int n = v.size();
    int k, aux;
    k = n + 1;
    while (k >= 1) {
        k /= 2;
        for (int i = 0; i + k < n; i++){
            aux = v[i + k];
            int j = i;
            while (j >= 0 && aux < v[j]){
                j -= k;
            }
            for (int h = i + k; h > j + k; h -= k){
                v[h] = v[h - k];
            }
            v[j + k] = aux;
        }
    }
}

void quickSort(vector<int> &v, int inicio, int fin){
    int k = inicio;
    int izq = inicio;
    int der = fin;
    int pivote = v[inicio];

    while (izq < der) {
        for (der; der > izq; der--) {
            if (v[der] < pivote) {
                v[k] = v[der];
                v[der] = pivote;
                k = der;
                break;
            }
        }
        for (izq; izq < der; izq++) {
            if (v[izq] > pivote) {
                v[k] = v[izq];
                v[izq] = pivote;
                k = izq;
                break;
            }
        }
    }

    if (inicio < k - 1) {
        quickSort(v, inicio, k - 1);
    }
    if (k + 1 < fin) {
        quickSort(v, k + 1, fin);
    }
}