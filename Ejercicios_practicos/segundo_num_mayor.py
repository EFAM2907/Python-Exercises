nums = [12, 7, 25, 3, 25, 18, 31, 31, 5, 10, 8]
mayor = float('-inf')
segundo_mayor = float('-inf')
tercer_mayor = float('-inf')
cuarto_mayor = float('-inf')

for i in nums:
    if i > mayor:
        cuarto_mayor = tercer_mayor
        tercer_mayor = segundo_mayor
        segundo_mayor = mayor
        mayor = i
    elif i > segundo_mayor:
        cuarto_mayor = tercer_mayor
        tercer_mayor = segundo_mayor
        segundo_mayor = i
    elif i > tercer_mayor:
        cuarto_mayor = tercer_mayor
        tercer_mayor = i
    elif i > cuarto_mayor:
        cuarto_mayor = i
    

print(mayor, segundo_mayor,tercer_mayor, cuarto_mayor)





#for i in nums:
#    if i > mayor:
 #       segundo_mayor = mayor
 #       mayor = i
 #   elif i > segundo_mayor:
 #       segundo_mayor = i
    
    