import sqlite3

# Abrir conexion

con = sqlite3.connect("data/peliculas.sqlite")

# Crear cusor
cur = con.cursor()

cur.execute("select id, nombre, url_foto, url_web from directores")

columns_description = cur.description

# Proceso la respuesta si la hubiera (un select)

result = cur.fetchall()



# hacer una funcion que me transforme la lista de tuplas result, en una lista de diccionarios como la que duvuelve el dict reader.

def transformar_en_diccionario(result):

# Claves:
    descripcion = ('id','Nombre', 'url_foto', 'url_web')
    lista = []

# Iterar sobre la lista de tuplas, crear diccionarios por iteracion y añadir a lista.
    for item in result:
        d = dict(zip(descripcion, item))
        lista.append(d)
        
    return lista

print(transformar_en_diccionario(result))
 

#Cerrar  la consexion siempre

con.close()