archivo_sin_leer = open("archivos_txt\\leer_text.txt", encoding= 'UTF-8')

#leer archivo completo
archivo = archivo_sin_leer.read()

#leer por lineas 
#lineas = archivo_sin_leer.readlines()
#linea = archivo_sin_leer.readline(23) # puede decidir que cantidad de caracteres para leer

print(archivo)