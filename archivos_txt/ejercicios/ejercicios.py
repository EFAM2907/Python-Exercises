nombre = ['edwin', 'angie', 'liliana', 'valen']
edad = ['24', '21', '39', '9']

#escribiendo archivo txt con dos listas diferentes

with open('archivos_txt\\ejercicio_txt', 'w') as archivo :
    
    #para una sola linea es importante solo el write
    archivo.write('los nombre y las edades son: \n\n')
    
    #lo metemos dentro de una lista['para poder hacer el for en una sola linea']
    archivo.writelines([ f'El nombre es: {n}\n la edad: {e}\n -------------\n' for n,e in zip(nombre,edad)])
    
    #la manera mas optima seria:
   # archivo.writelines([
    #    f'El nombre es {n}, la edad es {e}\n-------------\n'
    #    for n, e in zip(nombre, edad)
   # ])
   
   #esto seria igual a la parte anterior
    #for n, e in zip(nombre, edad):

    #    archivo.write(
    #        f'El nombre es: {n}\n'
    #       f'La edad es: {e}\n'
    #       f'-------------\n'
    #   )