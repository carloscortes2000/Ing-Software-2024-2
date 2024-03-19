from sqlalchemy import Column, Integer, String, Boolean, LargeBinary
from datetime import *
from alchemyClasses import db

class Usuario(db.Model):

    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido_Paterno = Column(String(100), nullable=False)
    apellido_Materno = Column(String(100), nullable=False)
    correo = Column(String(100), default=None, nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    fotoPerfil = Column(LargeBinary, nullable=False)
    superUsuario = Column(Boolean, nullable=False, default=False)

    def __init__(self, nombre, apellido_Paterno, apellido_Materno, password, email, profilePicture=None, superUser=None):
        self.nombre = nombre
        self.apellido_Paterno = apellido_Paterno
        self.apellido_Materno = apellido_Materno
        self.password = password
        self.email = email
        self.profilePicture = profilePicture
        self.superUser = superUser

     def __str__(self):
        return (f"<Usuarios(idUsuario='{self.idUsuario}', nombre='{self.nombre}', apellido_Paterno='{self.apellido_Paterno}', apellido_Materno='{self.apellido_Materno}', password='{self.password}', email='{self.email}', superUser='{self.superUser}')>")