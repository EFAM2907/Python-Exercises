nums = [5, 8, 10, 3, 7, 12]

def es_par(numero):
    return numero % 2 == 0


def obtener_pares(nums):
    return [num for num in nums if es_par(num)]

print(obtener_pares(nums))
