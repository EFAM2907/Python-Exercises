import csv

with open ('archivos_txt\\leer.csv') as archivo:
    reader = csv.reader(archivo)
    print(reader)