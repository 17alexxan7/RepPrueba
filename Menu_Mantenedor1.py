def mostrar_menu_mantenedor():
    print("MANTENEDOR USUARIO")
    print("[1] - Agregar usuario")
    print("[2] - Editar usuario")
    print("[3] - Eliminar usuario")
    print("[4] - Buscar usuario")
    print("[5] - Volver")

def cargar_datos(mibiblioteca):
    try:
        with open(mibiblioteca, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"usuarios": [], "libros": []}

def guardar_datos(mibiblioteca, datos):
    with open(mibiblioteca, 'w') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)

def agregar_usuario(datos, usuario):
    datos['usuarios'].append(usuario)

def editar_usuario(datos, usuario_id, nuevo_usuario):
    for usuario in datos['usuarios']:
        if usuario['id'] == usuario_id:
            usuario.update(nuevo_usuario)
            break

def eliminar_usuario(datos, usuario_id):
    datos['usuarios'] = [usuario for usuario in datos['usuarios']if usuario['id'] != usuario_id]

def buscar_usuario(datos, usuario_id):
    for usuario in datos['usuarios']:
        if usuario['id'] == usuario_id:
            return usuario
    return None
