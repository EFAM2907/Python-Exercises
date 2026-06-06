import pandas as pd

#leemos el cvs con pandas y lo guardamos en una variable, df = data frame
df = pd.read_csv('archivos_generales\\archivos_csv\\leer.csv')
df2 = pd.read_csv('archivos_generales\\archivos_csv\\leer.csv')

print(type(df))

#eliminamos valores nulos
#df = df.dropna()
#df2 = df2.dropna()

#lo ordenamos por edad, menor a mayor a viceversa con ascending en False
edades = df.sort_values("edad", ascending=False)
#print(edades)

#concatenando con la fucion concat de pandas
concatenado = pd.concat([df, df2])
#con drop_duplicates eliminamos filas repetidas- delate repeated rows
df_clean = concatenado.drop_duplicates()
print(df_clean)

df_clean.to_csv('archivos_generales\\archivos_csv\\leer_limpio.csv')
