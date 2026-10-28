import pandas as pd

df = pd.read_csv('../results/Datos.csv')

tiempo = df.groupby(['Algoritmo', 'n', 'Patron'])['Tiempo_ms'].agg(['mean', 'median', 'std', 'min', 'max']).reset_index().round(4)
print(tiempo)

operaciones = df.groupby(['Algoritmo', 'n', 'Patron'])[['Comparaciones', 'Intercambios']].agg(['mean', 'median', 'std', 'min', 'max']).reset_index().round(4)
print(operaciones)

df_100k = df[df['n'] == 100000]
mayor_esc = df_100k.groupby(['Algoritmo', 'Patron'])[['Tiempo_ms', 'Comparaciones', 'Intercambios']].agg(['mean', 'median', 'std', 'min', 'max']).reset_index().round(4)
print(mayor_esc)