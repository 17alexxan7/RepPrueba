import json

def generar_reporte(datos):
    categorias = {}
    for libro in datos['libros']:
        categoria = libro.get('categoria', 'Desconocida')
        if categoria in categorias:
            categorias[categoria] += 1
        else:
            categorias[categoria] = 1
    return categorias

def guardar_reporte(reporte, nombre_archivo):
    with open(mibiblioteca, 'w') as archivo:
        json.dump(reporte, archivo, ensure_ascii=False, indent=4)
