from abc import ABC, abstractmethod
import csv

class Model(ABC):
    @classmethod
    @abstractmethod
    def create_from_dict(cls, diccionario):
        pass

class Director(Model):
    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(diccionario["nombre"], int(diccionario["id"]))

    def __init__(self, nombre: str, id: int = -1):
        self.nombre = nombre
        self.id = id

    def __repr__(self) -> str:
        return f"Director ({self.id}): {self.nombre}"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.id == other.id and self.nombre == other.nombre
        return False
    
    def __hash__(self):
        return hash((self.id, self.nombre))


class Pelicula(Model):
    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(diccionario["titulo"], 
                   diccionario["sinopsis"], 
                   int(diccionario["director_id"]), 
                   int(diccionario["id"]))
    
    def __init__(self, titulo: str, sinopsis: str, director: object, id = -1):
        self.titulo = titulo
        self.sinopsis = sinopsis
        self.id = id
        self.director = director
                
    @property
    def director(self):
        return self._director
    
    @director.setter
    def director(self, value):
        if isinstance(value, Director):
            self._director = value
            self._id_director = value.id
        elif isinstance(value, int):
            self._director = None
            self._id_director = value
        else:
            raise TypeError(f"{value} debe ser un entero o instancia de Director")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.titulo == other.titulo and self.sinopsis == other.sinopsis and self.director == other.director and self.id == other.id
        return False
    
    def __hash__(self):
        return hash((self.id, self.titulo, self.sinopsis, self.director))
    
    def __repr__(self):
        return f"Pelicula ({self.id}): {self.titulo}, {self.director}"
    
class Genero(Model):
    @classmethod
    def create_from_dict(cls, diccionario):
            return cls(diccionario["genero"], int(diccionario["id"]))

    def __init__(self, genero: str, id: int = -1):
        self.genero = genero
        self.id = id

    def __repr__(self) -> str:
        return f"Genero ({self.id}): {self.genero}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.genero == other.genero and self.id == other.id
        return False

    def __hash__(self):
        return hash((self.id, self.genero))

class Copias(Model):

    @classmethod
    def create_from_dict(cls, diccionario):
            return cls(int(diccionario["id"]), int(diccionario["id_pelicula"]))

    def __init__(self, id_pelicula: int, id: int = -1 ):
        self.id_pelicula = id_pelicula 
        self.id = id

    def __repr__(self) -> str:
        return f"Genero ({self.id}): {self.id_pelicula}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.id_pelicula == other.id_pelicula and self.id == other.id
        return False

    def __hash__(self):
        return hash((self.id, self.id_pelicula))
    

 