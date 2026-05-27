import sys 
#usando sys para caarpetas atras de nuestra ruta
sys.path.append('c:\\Users\\Usuario\\Desktop\\Curso python Dalto\\tipos de datos')
print(sys.path)

import password

print(password.random_password(45))