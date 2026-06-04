import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Graficos\\ventas.csv')


# creando con matplotlib
# el primer valor sera igual al eje X y el segundo al eje Y
plt.plot(df['fecha'], df['cantidad_productos'])
plt.title('Productos vendidos')
plt.xlabel('Fecha')
plt.ylabel('Cantidad')
#mostrando el grafico
plt.show()

#creando con seaborn
#sns.lineplot(data= df, x ='fecha', y = 'cantidad_productos')
#plt.title('Productos Vendidos')
#plt.show()


