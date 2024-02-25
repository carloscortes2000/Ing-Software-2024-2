import pymysql.cursors
from datetime import datetime, timedelta
from faker import Faker
import random
# Nos ayuda a generar datos ficticios de manera realista.
fake = Faker()
# Variable global para la conexión a la base de datos
conectarse_a_bade_de_datos = pymysql.connect(
    host='localhost',
    user='lab',
    password='Developer123!',
    database='lab_ing_software',
    cursorclass=pymysql.cursors.DictCursor
)

# Función para insertar registros en cada tabla
def ingresar_registros():
    with conectarse_a_bade_de_datos.cursor() as cursor:
        # Insertar un usuario
        id_usuario = None
        nombre = fake.first_name()
        ap_pat = fake.last_name()
        ap_mat = fake.last_name()
        password = fake.password()
        email = fake.email()
        super_user = random.choice([0, 1])
        profile_picture = None
        sql = "INSERT INTO usuarios (idUsuario, nombre, apPat, apMat, password, email, profilePicture, superUser) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (id_usuario, nombre, ap_pat, ap_mat, password, email, profile_picture, super_user))
        
        # Insertar una película
        id_pelicula = None  # Se deja como None para que se autoincremente
        nombre_pelicula = fake.name()
        genero = fake.random_element(elements=('Acción', 'Comedia', 'Drama', 'Aventura', 'Ciencia Ficción'))
        duracion = random.randint(60, 180)
        inventario = random.randint(1, 50)
        sql = "INSERT INTO peliculas (idPelicula, nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (id_pelicula, nombre_pelicula, genero, duracion, inventario))
        
        # Insertar una renta
        id_rentar = None  
        id_usuario = random.randint(1, 1000)
        id_pelicula = random.randint(1, 1000)
        fecha_renta = fake.date_time_this_year()
        dias_de_renta = random.randint(1, 10)
        estatus = random.choice([0, 1])
        sql = "INSERT INTO rentar (idRentar, idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (id_rentar, id_usuario, id_pelicula, fecha_renta, dias_de_renta, estatus))
    
    conectarse_a_bade_de_datos.commit()
    print("Los registros fueron ingresados.")

# Función que filtra el apellido de un usuario dada una cadena especifica por el usuario
def filtrar_usuario_por_apellido(apellido):
    with conectarse_a_bade_de_datos.cursor() as cursor:
        sql = "SELECT * FROM usuarios WHERE apPat LIKE %s OR apMat LIKE %s"
        cursor.execute(sql, ('%' + apellido + '%', '%' + apellido + '%'))
        resultado = cursor.fetchall()
        for row in resultado:
            print(row)

# Función que cambia el género de una película
def cambiar_genero(movie_name, new_genre):
    with conectarse_a_bade_de_datos.cursor() as cursor:
        sql = "UPDATE peliculas SET genero = %s WHERE nombre = %s"
        cursor.execute(sql, (new_genre, movie_name))
    conectarse_a_bade_de_datos.commit()
    print("Se han cambiado el genero de la pelicula.")

# Función para eliminar rentas anteriores a 3 dias después de ejecutarse esta función
def elimina_renta():
    with conectarse_a_bade_de_datos.cursor() as cursor:
        tiempo_limite = datetime.now() - timedelta(days=3)
        sql = "DELETE FROM rentar WHERE fecha_renta <= %s"
        cursor.execute(sql, (tiempo_limite,))
    conectarse_a_bade_de_datos.commit()
    print("Rentas antiguas eliminadas exitosamente.")

# Ejecutar las funciones

ingresar_registros()
filtrar_usuario_por_apellido('Perez')
cambiar_genero('Matrix', 'Drama')
elimina_renta()

# Cerrar la conexión a la base de datos al final del programa
conectarse_a_bade_de_datos.close()



