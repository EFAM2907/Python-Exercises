#calculando la edad,con manejo de errores

año_actual = 2026


try:
    fecha_nacimiento = int(input('en que año naciste: '))
    if fecha_nacimiento > año_actual:
        print('venis del futuro?')
    elif fecha_nacimiento <= 0:
        print('que sos, jesucristo?')
    
    else:
        edad_actual = año_actual - fecha_nacimiento
        print(f'tu edad es {edad_actual} años')
     
except ValueError:
    print('debe ser un numero papi')

