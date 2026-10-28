import pandas as pd

df = pd.read_csv('../results/Datos.csv')

tiempo = df.groupby(['Algoritmo', 'n', 'Patron'])['Tiempo_ms'].agg(['mean', 'median', 'std', 'min', 'max']).reset_index().round(4)
tiempo.columns = ['Algoritmo', 'n', 'Patron', 'Promedio', 'Mediana', 'Dispersion_estandar', 'Minimo', 'Maximo']
tiempo.to_csv('../results/Resumen_tiempo.csv', index = False)

operaciones = df.groupby(['Algoritmo', 'n', 'Patron'])[['Comparaciones', 'Intercambios']].agg(['mean', 'median', 'min', 'max']).reset_index().round(2)
operaciones.columns = ['Algoritmo', 'n', 'Patron', 'Com_promedio', 'Com_mediana', 'Com_minimo', 'Com_maximo', 'Int_promedio', 'Int_mediana', 'Int_minimo', 'Int_maximo']
operaciones.to_csv('../results/Resumen_operaciones.csv', index = False)

df_100k = df[df['n'] == 100000]
mayor_esc = df_100k.groupby(['Algoritmo', 'Patron'])[['Tiempo_ms', 'Comparaciones', 'Intercambios']].agg('mean').reset_index().round(2)
mayor_esc.columns = ['Algoritmo', 'Patron', 'Ti_promedio', 'Com_promedio', 'Int_promedio']
mayor_esc.to_csv('../results/Resumen_100k.csv', index = False)

df_quicksort = df[df['Algoritmo'] == 'QuickSort']
profundidad = df_quicksort.groupby(['n', 'Patron'])['Profundidad_Recursion'].agg(['mean', 'max']).reset_index().round(2)
profundidad.columns = ['n', 'Patron', 'Promedio', 'Maximo']
profundidad.to_csv('../results/Resumen_profundidad.csv', index = False)