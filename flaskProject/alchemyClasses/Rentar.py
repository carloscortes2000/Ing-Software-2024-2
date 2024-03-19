from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, LargeBinary
from datetime import *
from alchemyClasses import db


class Rentar(db.Model):
    __tablename__ = 'rentas'
    idRentar = Column(Integer, primary_key=True, autoincrement=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'), nullable=False)
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'), nullable=False)
    fecha_renta = Column(DateTime, nullable=False)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Boolean, nullable=True)


    def __init__(self, idUsuario, idPelicula, fecha_Renta=date.today(), dias_de_renta=5, estatus=False):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

    def __str__(self):
        return (f"<Rentar(idRentar='{self.idRentar}', idUsuario='{self.idUsuario}', idPelicula='{self.idPelicula}', fecha_renta='{self.fecha_renta}', dias_de_renta='{self.dias_de_renta}', estatus='{self.estatus}')>")