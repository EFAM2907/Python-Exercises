#recreando las tablas de multiplicar de una manera facil

#numero = input('dame un numero entre 1 y 10: ')



#if numero.isdigit() and numero >= 1 and numero <= 10 :
 #   numero = int(numero)
 #   for num in range(1,11) :
  #      print(numero,'x',num,'=', numero * num )
#else :
 #   print('te dije que un numero ome') 

print('usando el while primeros pasos')

while True:
    try:
        numero = int(input('Dame un numero del 1 al 10: '))
        print("Leí:", numero)
        if numero >= 1 and numero <= 10 :
          for num in range(1,11):
            print(numero,'x',num,'=',numero * num)
            
          print('voy a hacer un while')
          break
      
        else:
         print('No te pases, es de 1 a 10')
         
    except ValueError:
         print('te dije un numero bro')
         
         
         
print('se termino el while')