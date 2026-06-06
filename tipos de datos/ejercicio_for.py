#desarrollar un adgoritmo que permita ingresar cierta cantida de personas, 
# la computadora debe pedir la edad de cada uno,
# y finalmente mostrar el porcentaje de personas que es mayor de edad


personas = []


try:
    cantidad_personas = int(input('dame un numero de persona: '))
    for persona in range(cantidad_personas):
      nombre = input('dame tu nombre crack: ')
      edad = int(input('tu edad es: '))
      personas.append((nombre, edad))
        
    mayores_de_edad = 0

    for nombre,edad in personas :
     if edad >= 18:
        mayores_de_edad += 1
        
        procentaje_mayores = (mayores_de_edad/cantidad_personas) * 100
        print(f'el porcentaje de mayores de edad son : {procentaje_mayores} %')  
except ValueError:
    print('dije un numero')   

