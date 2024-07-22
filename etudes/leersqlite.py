import sqlite3

# Abrir conexion

con = sqlite3.connect("data/peliculas.sqlite")

# Crear cusor
cur = con.cursor()

cur.execute("select id, nombre, url_foto, url_web from directores")

# Proceso la respuesta si la hubiera (un select)

result = cur.fetchall()

print(result)

#Cerrar  la consexion siempre

con.close()