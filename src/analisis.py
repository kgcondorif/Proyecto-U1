import pandas as pd

df = pd.read_csv('../results/Datos.csv')

tiempo = df.groupby(['Algoritmo', 'n', 'Patron'])['Tiempo_ms'].agg(['mean', 'median', 'std', 'min', 'max']).reset_index().round(4)
tiempo.columns = ['Algoritmo', 'n', 'Patron', 'Promedio', 'Mediana', 'Dispersion_estandar', 'Minimo', 'Maximo']
print(tiempo)

operaciones = df.groupby(['Algoritmo', 'n', 'Patron'])[['Comparaciones', 'Intercambios']].agg(['mean', 'median', 'min', 'max']).reset_index().round(2)
operaciones.columns = ['Algoritmo', 'n', 'Patron', 'Com_promedio', 'Com_mediana', 'Com_minimo', 'Com_maximo', 'Int_promedio', 'Int_mediana', 'Int_minimo', 'Int_maximo']
print(operaciones)

df_100k = df[df['n'] == 100000]
mayor_esc = df_100k.groupby(['Algoritmo', 'Patron'])[['Tiempo_ms', 'Comparaciones', 'Intercambios']].agg('mean').reset_index().round(2)
mayor_esc.columns = ['Algoritmo', 'Patron', 'Ti_promedio', 'Com_promedio', 'Int_promedio']
print(mayor_esc)