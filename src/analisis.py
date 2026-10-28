import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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


sns.set_theme(style="whitegrid")

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.lineplot(
    data=df, x='n', y='Tiempo_ms', hue='Algoritmo', style='Patron',
    markers=True, dashes=False, errorbar=None, ax=ax1
)
ax1.set_title("Escalabilidad: Tamaño de Entrada (n) vs Tiempo de Ejecución (ms)")
ax1.set_xlabel("Tamaño de Entrada (n)")
ax1.set_ylabel("Tiempo Promedio (ms)")
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
fig1.tight_layout()

fig1.savefig('../results/Grafico_N_vs_Tiempo.png', dpi=300)
plt.close(fig1)

fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.boxplot(data=df, x='Patron', y='Tiempo_ms', hue='Algoritmo', ax=ax2)
ax2.set_title("Distribución de Tiempos por Patrón de Entrada (30 Repeticiones)")
ax2.set_xlabel("Patrón de Entrada")
ax2.set_ylabel("Tiempo de Ejecución (ms)")
plt.setp(ax2.get_xticklabels(), rotation=45)
ax2.legend(loc='upper right')
fig2.tight_layout()

fig2.savefig('../results/Patrones.png', dpi=300)
plt.close(fig2)

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.lineplot(
    data=df, x='n', y='Comparaciones', hue='Algoritmo', style='Patron',
    markers=True, dashes=False, errorbar=None, ax=ax3
)
ax3.set_title("Análisis Operacional: Tamaño de Entrada (n) vs Número de Comparaciones")
ax3.set_xlabel("Tamaño de Entrada (n)")
ax3.set_ylabel("Comparaciones Promedio")
ax3.set_xscale('log')
ax3.set_yscale('log')
ax3.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
fig3.tight_layout()

fig3.savefig('../results/Grafico_N_vs_Comparaciones.png', dpi=300)
plt.close(fig3)