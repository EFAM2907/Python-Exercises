Cantidad_de_números = 0  #check
Suma= 0
Promedio= 0
Mayor= float('-inf')
Menor= float('inf')
Cantidad_de_pares= 0
Cantidad_de_impares= 0

nums = [12, 7, 25, 3, 18, 31, 5, 10, 8]



for i in range(len(nums)):
    Cantidad_de_números = i +1
    Suma+= nums[i]
    Promedio = Suma // Cantidad_de_números
    
    if nums[i] > Mayor:
        Mayor = nums[i]   
    if nums[i] < Menor:
        Menor = nums[i] 
    if nums[i] % 2 == 0:
        Cantidad_de_pares += 1
    else:
        Cantidad_de_impares += 1
        
   
   
        

print(Cantidad_de_impares, 'cantidad de impares')
print(Cantidad_de_pares, ' cantidad de pares')
print(Mayor, 'mayor')
print(Menor, 'menor')
print(Cantidad_de_números, 'cantidad')
print(Suma, 'suma')
print(Promedio, 'promedio')
