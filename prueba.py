import json
def mostrar_menu_principal():
    print("MUNDO LIBRO")
    print("1- Mantenedor de usuarios")
    print("2- Reportes")
    print("3- Salir")

def main():
    datos = cargar_datos('bibliotecajson.json')
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                mostrar_menu_mantenedor()
                subopcion = input("Seleccione una opción: ")

                if subopcion == "1":
                    id_usuario = input("Ingrese ID del usuario: ")
                    nombre = input("Ingrese nombre del usuario: ")
                    email = input("Ingrese email del usuario: ")
                    fecha_registro = input("Ingrese fecha de registro del usuario: ")
                    nuevo_usuario = {"id": id_usuario, "nombre": nombre, "email": email, "fechaRegistro": fecha_registro}
                    agregar_usuario(datos, nuevo_usuario)
                    guardar_datos('bibliotecajson.json', datos)
                    print("Usuario agregado con éxito.")
                
                elif subopcion == "2":
                    id_usuario = input("Ingrese ID del usuario a editar: ")
                    nombre = input("Ingrese nuevo nombre del usuario: ")
                    email = input("Ingrese nuevo email del usuario: ")
                    fecha_registro = input("Ingrese nueva fecha de registro del usuario: ")
                    nuevo_usuario = {"nombre": nombre, "email": email, "fechaRegistro": fecha_registro}
                    editar_usuario(datos, id_usuario, nuevo_usuario)
                    guardar_datos('bibliotecajson.json', datos)
                    print("Usuario editado con éxito.")
                
                elif subopcion == "3":
                    id_usuario = input("Ingrese ID del usuario a eliminar: ")
                    eliminar_usuario(datos, id_usuario)
                    guardar_datos('bibliotecajson.json', datos)
                    print("Usuario eliminado con éxito.")
                
                elif subopcion == "4":
                    id_usuario = input("Ingrese ID del usuario a buscar: ")
                    usuario = buscar_usuario(datos, id_usuario)
                    if usuario:
                        print(f"Usuario encontrado: {usuario}")
                    else:
                        print("Usuario no encontrado.")
                
                elif subopcion == "5":
                    break
                
        
        elif opcion == "2":
            reporte = generar_reporte(datos)
            guardar_reporte(reporte, 'Reportes_biblioteca_mundo_libro.json')
            print("Reporte generado y guardado con éxito.")
        
        elif opcion == "3":
            break