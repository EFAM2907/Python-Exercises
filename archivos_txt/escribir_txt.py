with open ('archivos_txt\\leer_text.txt','w', encoding='UTF-8') as archivo:
    archivo.writelines(['probando escritura de txt\n','salto de linea, segunda parte aqui'])
    #wirtelines sobre escribe el archivo
    
    archivo.writelines(['probando nuevo texto sin sobreescribir\n','salto de linea, segunda parte aqui'])
    #wirtelines si lo uso dos veces, no sobre escribe la anterior, solo me da una linea mas