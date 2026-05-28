import pandas as pd

#leemos el cvs con pandas y lo guardamos en una variable, df = data frame
df = pd.read_csv('archivos_txt\\leer.csv')
df2 = pd.read_csv('archivos_txt\\leer.csv')

#lo ordenamos por edad, menor a mayor a viceversa con ascending en False
edades = df.sort_values("edad", ascending=False)
#print(edades)

concatenado = pd.concat([df, df2])
print(concatenado)