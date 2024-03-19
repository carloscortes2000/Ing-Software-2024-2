from sqlalchemy import Column, Integer, String
from alchemyClasses import db

class Pelicula(db.Model):

    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    genero = Column(String(45))
    duracion = Column(Integer)
    inventario = Column(Integer, default=1, nullable=False)

    def __init__(self, nombre, genero=None, duracion=None, inventario):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return (f'Pelicula: {self.nombre} Genero: {self.genero} Duracion: {self.duracion} Inventario: {self.inventario}')