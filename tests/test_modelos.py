from app.modelos import Director, DaoCsvDirector, Pelicula, DaoCsvPelicula

def test_create_director():
    director = Director("Robert Redford")

    assert director.nombre == "Robert Redford"
    assert director.id == -1


def test_dao_directores_traer_todos():
    dao = DaoCsvDirector("tests/data/directores.csv")
    directores = dao.todos()

    assert len(directores) == 8
    assert directores[7] == Director("Charlie Chaplin", 8) 

def test_create_pelicula():
    pelicula = Pelicula("El señor de los anillos", "Sauron es muy malo", 9)

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es muy malo"
    assert pelicula._id_director == 9
    assert pelicula.id == -1
    assert pelicula.director is None
  
def test_create_pelicula_and_informar_director_completo():
    director = Director("Peter Jackson", 9)
    pelicula = Pelicula("El señor de los anillos", "Sauron es muy malo", director)

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es muy malo"
    assert pelicula._id_director == 9
    assert pelicula.id == -1
    assert pelicula.director == director

def test_asigna_director_a_pelicula():
    pelicula = Pelicula("El señor de los anillos", "Sauron es muy malo", -1)

    director = Director("Peter Jackson", 9)

    pelicula.director = director

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es muy malo"

    assert pelicula.id == -1
    assert pelicula.director == director
    assert pelicula._id_director == 9

def test_dao_peliculas_traer_todos():
    dao = DaoCsvPelicula("tests/data/peliculas-2.csv")
    peliculas = dao.todos()

    assert len(peliculas) == 5
    assert peliculas[4] == Pelicula("Psicosis", "Una joven secretaria, tras cometer un robo, se marcha de la ciudad y conduce durante horas, parando para descansar en un pequeño motel de carretera regentado por un joven llamado Norman. Todo parece normal y tranquilo en el apartado motel y en la casa de al lado en la que viven Norman y su madre pero, mientras está en la ducha, la joven es asesinada salvajemente a cuchilladas.", 3, 24)




 