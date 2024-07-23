from abc import ABC, abstractmethod
from app.modelos import Director, Pelicula, Genero, Copias
import csv
import sqlite3

class DAO(ABC):
    """
    @abstractmethod
    def guardar(self, instancia):
        pass
    
    @abstractmethod
    def actualizar(self, instancia):
        pass
    
    @abstractmethod
    def borrar(self, id: int):
        pass
    
    @abstractmethod
    def consultar(self, id: int):
        pass
    """

    @abstractmethod
    def todos(self):
        pass

class DAO_CSV(DAO):
    model = None

    def __init__(self, path):
        self.path = path

    def todos(self):
        with open(self.path, "r", newline="", encoding="utf-8") as fichero:
            lector_csv = csv.DictReader(fichero, delimiter=";", quotechar="'")
            lista = []
            for registro in lector_csv:
                lista.append(self.model.create_from_dict(registro))
        return lista 

class DAO_SQLite(DAO):
    model = None
    tabla = None

    def __init__(self, path) -> None:
        self.path = path

    def todos(self):
        """
        acceder a sqlite y traer todos los registros de la tabla del modelo
        con la funcion rows_to_dictlist traerlos en forma de diccionario
        devolverlos como instancias de Model
        """
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()

        cur.execute(f"select * from {self.tabla}")
        
        nombres = list(map(lambda item: item[0], cur.description))

        lista = self.__rows_to_dictlist(cur.fetchall(), nombres)
        resultado = []
        # Evitar este segundo bucle (es segundo porque el primero está en la linea 136) haciendo que
        # rows_to_dicc... devuelva una lista de Modelos y no una lista de diccionarios
        for registro in lista:
            resultado.append(self.model.create_from_dict(registro))

        conn.close()

        return resultado

    def __rows_to_dictlist(self, filas, nombres):
        registros = []
        for fila in filas:
            registro = {}
            pos = 0
            for nombre in nombres:
                registro[nombre] = fila[pos]
                pos += 1

            """
            for pos, nombre in enumerate(nombres):
                registro[nombre] = fila[pos]
            """
            registros.append(registro)
        return registros






class DAO_SQLite_Director(DAO_SQLite):
    model = Director
    tabla = "directores"


class DAO_CSV_Director(DAO_CSV):
    model = Director

class DAO_CSV_Pelicula(DAO_CSV):
    model = Pelicula

class DAO_CSV_Genero(DAO_CSV):
    model = Genero    

class DAO_CSV_Copias(DAO_CSV):
    model = Copias    

         