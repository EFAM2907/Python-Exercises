#importante recordar que el segundo parametro en este caso 'a' describi que haremos con el archivo a,w...

with open ('archivos_txt\\leer_text.txt','a', encoding='UTF-8') as archivo:
    archivo.write('\n')
    for i in range(4):
     archivo.write(f'linea {i+1} agregada\n')