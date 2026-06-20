#detectar cual es el numero maximo y minimo ingresado por el usuario

cantidad_de_numeros = 4 
numero_maximo = float('-inf')
numero_minimo = float('inf')

for num in range( cantidad_de_numeros):
    numeros = int(input('el numero es: '))
    if numeros > numero_maximo:
        numero_maximo = numeros
    else :
        numeros < numero_minimo
        numero_minimo = numeros
        
        
print(f'el numero maximo es {numero_maximo}')
print(f'el numero minimo es {numero_minimo}')





        
    