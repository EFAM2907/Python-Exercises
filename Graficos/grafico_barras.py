import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Graficos\\fuente_ingresos.csv')


# creando con matplotlib
# el primer valor sera igual al eje X y el segundo al eje Y
#plt.bar(df['fuente'], df['ingreso'])
#plt.title('Fuente de ingresos')
#plt.xlabel('Fecha')
#plt.ylabel('Cantidad')
#mostrando el grafico
#plt.show()

sns.barplot(data= df, x ='fuente', y = 'ingreso')
plt.title('Fuente de ingresos')
#total_ingresos = f'los ingresos totales son : {df['ingreso'].sum()}'
#print(total_ingresos)
plt.show()