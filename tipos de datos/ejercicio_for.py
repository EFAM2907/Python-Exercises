#desarrollar un adgoritmo que permita ingresar cierta cantida de personas, 
# la computadora debe pedir la edad de cada uno,
# y finalmente mostrar el porcentaje de personas que es mayor de edad


poeple = []


try:
    number_of_people = int(input('Give me a numbers of people : '))
    for person in range(number_of_people):
      name = input('give me a name crack: ')
      age = int(input('age: '))
      poeple.append((name, age))
        
    adults = 0

    for name,age in poeple :
     if age >= 18:
        adults += 1
        
        adults_percentage  = round((adults/number_of_people) * 100)
        print(f'The percentage of adults is : {adults_percentage } %')  
except ValueError:
    print('I said a number gay')   


#Mismo con codigo pero con un manejo de errores mayor


#personas = []

#while True:
#    try:
 #       cantidad_personas = int(input('Dame un número de personas: '))
  #      if cantidad_personas <= 0:
  #          print('Por favor, ingresa un número mayor que cero.')
  #          continue
 #       break  # Si todo es correcto, salimos del bucle
 #   except ValueError:
#        print('Por favor, ingresa un número válido.')

#contador = 0
#while contador < cantidad_personas:
#    nombre = input('Dame tu nombre: ')
#    while True:
#        try:
#            edad = int(input('Tu edad es: '))
#            if edad < 0:
  #              print('La edad no puede ser negativa. Inténtalo de nuevo.')
 #               continue
 #           break  # Si la edad es válida, salimos del bucle
 #       except ValueError:
 #           print('Por favor, ingresa un número válido para la edad.')

 #   personas.append((nombre, edad))
 #   contador += 1

#mayores_de_edad = 0

#for nombre, edad in personas:
#    if edad >= 18:
#        mayores_de_edad += 1

#porcentaje_mayores = (mayores_de_edad / cantidad_personas) * 100

#print(f'El porcentaje de mayores de edad es: {porcentaje_mayores} %')