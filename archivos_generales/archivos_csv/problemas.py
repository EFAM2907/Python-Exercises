import pandas as pd

#leemos nuestro archivo con read_csv -- Reading a csv file
df = pd.read_csv('archivos_txt\\leer.csv')

#convertimos una columna a un tipo de dato, en este caso string -- converting a column to a data type
df['edad'] = df['edad'].astype(str)

#para mostrarlo solo acedemos a la columna, seguido de la posicicion en el indice --- to display it, we simply access the colum
#print(df['edad'][0])

#reemplazando el valor de una columna con replace -- replace a colunm value with .replace()
df['nombre']= df['nombre'].replace('Edwin','fernando', inplace=True) 

#con rename podemos cambiar el nombre de una columna --- rename usefull to change the colunm names, by colunm or even date with the index
df = df.rename(columns={'edad': 'Age', 'nombre': 'Name', 'apellido': 'Lastname'})
df = df.rename(index={ 0: 'vip_user'})#pendiente por consultar mas

print(df)
   
