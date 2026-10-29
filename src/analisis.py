import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('results/Datos.csv')

tiempo = df.groupby(['Algoritmo', 'n', 'Patron'])['Tiempo_ms'].agg(['mean', 'median', 'std', 'min', 'max']).reset_index().round(4)
tiempo.columns = ['Algoritmo', 'n', 'Patron', 'Promedio', 'Mediana', 'Dispersion_estandar', 'Minimo', 'Maximo']
tiempo.to_csv('results/Resumen_tiempo.csv', index = False)

operaciones = df.groupby(['Algoritmo', 'n', 'Patron'])[['Comparaciones', 'Intercambios']].agg(['mean', 'median', 'min', 'max']).reset_index().round(2)
operaciones.columns = ['Algoritmo', 'n', 'Patron', 'Com_promedio', 'Com_mediana', 'Com_minimo', 'Com_maximo', 'Int_promedio', 'Int_mediana', 'Int_minimo', 'Int_maximo']
operaciones.to_csv('results/Resumen_operaciones.csv', index = False)

df_100k = df[df['n'] == 100000]
mayor_esc = df_100k.groupby(['Algoritmo', 'Patron'])[['Tiempo_ms', 'Comparaciones', 'Intercambios']].agg('mean').reset_index().round(2)
mayor_esc.columns = ['Algoritmo', 'Patron', 'Ti_promedio', 'Com_promedio', 'Int_promedio']
mayor_esc.to_csv('results/Resumen_100k.csv', index = False)

df_quicksort = df[df['Algoritmo'] == 'QuickSort']
profundidad = df_quicksort.groupby(['n', 'Patron'])['Profundidad_Recursion'].agg(['mean', 'max']).reset_index().round(2)
profundidad.columns = ['n', 'Patron', 'Promedio', 'Maximo']
profundidad.to_csv('results/Resumen_profundidad.csv', index = False)


sns.set_theme(style = "whitegrid")
df_qs = df[df['Algoritmo'] == 'QuickSort']
df_ss = df[df['Algoritmo'] == 'ShellSort']

fig1, ax1 = plt.subplots(figsize = (10, 6))
sns.lineplot(
    data = df_qs, x = 'n', y = 'Tiempo_ms', style = 'Patron', hue = 'Patron',
    markers = True, dashes = False, errorbar = None, ax = ax1, linewidth = 2, markersize = 8
)
ax1.set_title("Fig. 1: QuickSort - Escalabilidad de Tiempo (ms)", fontsize = 12, fontweight = 'bold')
ax1.set_xlabel("Tamaño de Entrada (n log)", fontsize = 10)
ax1.set_ylabel("Tiempo Promedio (ms log)", fontsize = 10)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.legend(bbox_to_anchor=(1.05, 1), loc = 'upper left', frameon = True)
fig1.tight_layout()

fig1.savefig('results/Quicksort_N_vs_Tiempo.png', dpi = 300)
plt.close(fig1)

fig2, ax2 = plt.subplots(figsize = (10, 6))
sns.lineplot(
    data = df_qs, x = 'n', y = 'Comparaciones', style = 'Patron', hue = 'Patron',
    markers = True, dashes = False, errorbar = None, ax = ax2, linewidth = 2, markersize = 8
)
ax2.set_title("Fig. 2: QuickSort - Análisis Operacional de Comparaciones", fontsize = 12, fontweight = 'bold')
ax2.set_xlabel("Tamaño de Entrada (n log)", fontsize = 10)
ax2.set_ylabel("Comparaciones Promedio (log)", fontsize = 10)
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.legend(bbox_to_anchor = (1.05, 1), loc = 'upper left', frameon = True)
fig2.tight_layout()

fig2.savefig('results/Quicksort_N_vs_Comparaciones.png', dpi = 300)
plt.close(fig2)

fig3, ax3 = plt.subplots(figsize = (10, 6))
sns.lineplot(
    data = df_ss, x = 'n', y = 'Tiempo_ms', style = 'Patron', hue = 'Patron',
    markers = True, dashes = False, errorbar = None, ax = ax3, linewidth = 2, markersize = 8
)
ax3.set_title("Fig. 3: ShellSort - Escalabilidad de Tiempo (ms)", fontsize = 12, fontweight = 'bold')
ax3.set_xlabel("Tamaño de Entrada (n log)", fontsize = 10)
ax3.set_ylabel("Tiempo Promedio (ms log)", fontsize = 10)
ax3.set_xscale('log')
ax3.set_yscale('log')
ax3.legend(bbox_to_anchor = (1.05, 1), loc = 'upper left', frameon = True)
fig3.tight_layout()

fig3.savefig('../results/Shellsort_N_vs_Tiempo.png', dpi = 300)
plt.close(fig3)

fig4, ax4 = plt.subplots(figsize = (10, 6))
sns.lineplot(
    data = df_ss, x = 'n', y = 'Comparaciones', style = 'Patron', hue = 'Patron',
    markers = True, dashes = False, errorbar = None, ax = ax4, linewidth = 2, markersize = 8
)
ax4.set_title("Fig. 4: ShellSort - Análisis Operacional de Comparaciones", fontsize = 12, fontweight = 'bold')
ax4.set_xlabel("Tamaño de Entrada (n log)", fontsize = 10)
ax4.set_ylabel("Comparaciones Promedio (log)", fontsize = 10)
ax4.set_xscale('log')
ax4.set_yscale('log')
ax4.legend(bbox_to_anchor = (1.05, 1), loc = 'upper left', frameon = True)
fig4.tight_layout()

fig4.savefig('results/Shellsort_N_vs_Comparaciones.png', dpi = 300)
plt.close(fig4)

df_max_n = df[df['n'] == 100000]

fig5, ax5 = plt.subplots(figsize=(12, 6))
sns.barplot(
    data = df_max_n, x = 'Patron', y = 'Tiempo_ms', hue = 'Algoritmo',
    ax = ax5, errorbar = 'sd'
)
ax5.set_title(f"Fig. 5: Comparativa de Rendimiento por Patrón de Entrada (n = 100000)", fontsize = 12, fontweight = 'bold')
ax5.set_xlabel("Patrón de Entrada", fontsize = 10)
ax5.set_ylabel("Tiempo Promedio (ms)", fontsize = 10)
plt.setp(ax5.get_xticklabels(), rotation = 30, ha = 'right')
ax5.legend(loc = 'upper right', frameon = True)
for p in ax5.patches:
    height = p.get_height()
    if height > 0: 
        ax5.annotate(
            f'{height:.2f}', 
            (p.get_x() + p.get_width() / 2., height),
            ha = 'center', va = 'bottom',
            xytext = (0, 3),
            textcoords = 'offset points',
            fontsize = 9, fontweight = 'bold'
        )

ax5.set_ylim(0, ax5.get_ylim()[1] * 1.15)
fig5.tight_layout()

fig5.savefig('results/Rendimiento_comparativa.png', dpi = 300)
plt.close(fig5)