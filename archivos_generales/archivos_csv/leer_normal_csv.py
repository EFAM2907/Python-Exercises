import csv
#leyendo de forma facil
with open ('archivos_generales\\archivos_csv\\leer.csv', 'r') as archivo:
    #si usamos reader automaticamente nos devuelve una lista, es lo recomendado
    reader = csv.reader(archivo)
    print(reader)
    
    for L in reader:
        print(L)
    
    #si simplemente usamos for, python lo interpretara como solo un string
    #for i in archivo:
    #    print(i)