usuarios = [
    {"nombre": "Edwin", "edad": 24, "ciudad": "Medellín"},
    {"nombre": "Angie", "edad": 21, "ciudad": "Medellín"},
    {"nombre": "Liliana", "edad": 39, "ciudad": "Yolombó"}
]

def mostrar_usuarios(usuarios):
    for usuario in usuarios:
        print(f'{usuario["nombre"]} | {usuario["edad"]} | {usuario["ciudad"]}')


def buscar_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario['nombre'] == nombre:
           print(f'{usuario["nombre"]} | {usuario["edad"]} | {usuario["ciudad"]}')
           return
    print('usuario no encontrado')
            
            
buscar_usuario(usuarios, 'Anie')