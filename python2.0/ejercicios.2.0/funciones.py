usuarios = [
    {"nombre": "Edwin", "edad": 24, "ciudad": "Medellín"},
    {"nombre": "Angie", "edad": 21, "ciudad": "Medellín"},
    {"nombre": "Liliana", "edad": 39, "ciudad": "Yolombó"}
]

def mostrar_usuarios(usuarios):
    for usuario in usuarios:
        print(f'{usuario["nombre"]} | {usuario["edad"]} | {usuario["ciudad"]}')

def agregar_usuario(usuarios, nombre, edad, ciudad):
    usuarios.append({"nombre":nombre, "edad": edad, "ciudad": ciudad} )
            
def buscar_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario['nombre'].lower() == nombre.lower():
           print(f'{usuario["nombre"]} | {usuario["edad"]} | {usuario["ciudad"]}')
           return
    print('usuario no encontrado')

def actualizar_ciudad(usuarios, nombre, ciudad):
    for usuario in usuarios:
        if usuario['nombre'].lower() == nombre.lower():
            usuario['ciudad'] = ciudad
            print('ciudad actualizada')
            return 
    print('usuario no encontrado') 
    
def eliminar_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario['nombre'].lower() == nombre.lower():
           usuarios.remove(usuario)
           print('usuario eliminado')
           return
    print('usuario no encontrado')
    
    
while True:
    print("""
      ========= SISTEMA DE USUARIOS =========

1. Mostrar usuarios
2. Agregar usuario
3. Buscar usuario
4. Actualizar ciudad
5. Eliminar usuario
6. Salir
      """)

    opcion = input('selecione una opcion: ')
    
    if opcion == "1":
     mostrar_usuarios(usuarios)

    elif opcion == "2":
     nombre = input('nombre del usuario: ').strip()
     edad = int(input('edad del usuario: '))
     ciudad= input('ciudad del usuario: ').strip()
     agregar_usuario(usuarios, nombre, edad, ciudad)
   
    elif opcion == "3":
     nombre = input('nombre del usuario: ')   
     buscar_usuario(usuarios, nombre)

    elif opcion == "4":
        nombre = input('nombre del usuario: ').strip()
        ciudad = input('ciudad actual: ').strip()
        actualizar_ciudad(usuarios, nombre, ciudad)

    elif opcion == "5":
      nombre = input('nombre de usuario que deseas eliminar: ').strip()
      eliminar_usuario(usuarios, nombre)

    elif opcion == "6":
     print("Hasta luego")
     break



  

