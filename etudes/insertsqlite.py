import sqlite3

con = sqlite3.connect("data/peliculas.sqlite")

cur = con.cursor()

nombre = input("Nombre: ")
foto = input("Urll afoto: ")
web = input("url web: ")


cur.execute(f"INSERT INTO directores (nombre,url_foto, url_web) values ('{nombre}', '{foto}', '{web}')")


con.close()