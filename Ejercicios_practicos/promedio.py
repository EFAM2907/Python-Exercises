nums = [3, 8, 2, 8, 5, 8, 1]

mayores = []

for i in nums:
   if len(mayores) < 4:
       mayores.append(i)
   elif i > min(mayores):
       mayores.remove(min(mayores))
       mayores.append(i)
       

promedio = sum(mayores) / 4

print(promedio)



        
