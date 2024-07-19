import csv
"""
fichero = open("data/directores.csv", "r", newline="")

lector_csv = csv.reader(fichero, delimiter=";", quotechar="'")

for registro in lector_csv:
    print(registro)

fichero.close()

#ahora como diccionario.
fichero = open("data/directores.csv", "r", newline="")
lector_csv = csv.DictReader(fichero, delimiter=";", quotechar="'")

for registro in lector_csv:
    print(registro)


fichero.close() 
"""   


with open("data/grupos_zoo.csv", "r", newline='') as fichero:
    lector = csv.DictReader(fichero)
    for fila in lector:
        print(fila)
