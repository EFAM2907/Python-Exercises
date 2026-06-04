import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Graficos\\timeline.csv')


# creando con matplotlib
# el primer valor sera igual al eje X y el segundo al eje Y
plt.scatter(df['tiempo'], df['dinero'])
plt.title('Tiempo de inversion')
plt.xlabel('tiempo')
plt.ylabel('dinero')
#mostrando el grafico
plt.show()

#sns.scatter(data= df, x ='tiempo', y = 'dinero')
#plt.title('Tiempo de inversion')
#plt.show()
