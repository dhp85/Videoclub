from abc import ABC, abstractmethod
from app.modelos import Director, Pelicula, Genero, Copias
import csv

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

class DAO_CSV_Director(DAO_CSV):
    model = Director

class DAO_CSV_Pelicula(DAO_CSV):
    model = Pelicula

class DAO_CSV_Genero(DAO_CSV):
    model = Genero    

class DAO_CSV_Copias(DAO_CSV):
    model = Copias    