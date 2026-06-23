usuarios = [
    {"nombre": "Edwin", "edad": 24, "ciudad": "Medellín"},
    {"nombre": "Angie", "edad": 21, "ciudad": "Medellín"},
    {"nombre": "Liliana", "edad": 39, "ciudad": "Yolombó"}
]


def eliminar_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario['nombre'] == nombre:
           usuarios.remove(usuario)
        return
    
    return 'No esta rey'

eliminar_usuario(usuarios, "Edwin")


def actualizar_ciudad(usuarios, nombre, ciudad):
    for usuario in usuarios:
        if usuario['nombre'] == nombre:
            usuario['ciudad'] = ciudad
            print('si entro')
            return 
    print('usuario no encontrado') 


def agregar_usuario(usuarios, nombre, edad, ciudad):
    usuarios.append({"nombre":nombre, "edad": edad, "ciudad": ciudad} )
    
def mostrar_usuarios(usuarios):
    resultado = []

    for usuario in usuarios:
        resultado.append(f'{usuario["nombre"]} | {usuario["edad"]} | {usuario["ciudad"]}')

    return resultado

for linea in mostrar_usuarios(usuarios):
    print(linea)
    
    
