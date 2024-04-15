import React, { useState } from 'react';
import './CRUDPeliculas.css';

const CRUDPeliculas = () => {
    // Estado para almacenar la lista de películas
    const [peliculas, setPeliculas] = useState([]);
    // Estado para la nueva película a agregar
    const [nuevaPelicula, setNuevaPelicula] = useState({
        id: "",
        titulo: "",
        genero: "",
        duracion: "",
        inventario: ""
    });

    // Función para agregar una nueva película
    const agregarPelicula = () => {
        if (nuevaPelicula.titulo.trim() !== "" && nuevaPelicula.genero.trim() !== "" && nuevaPelicula.duracion.trim() !== "" && nuevaPelicula.inventario.trim() !== "") {
            setPeliculas([...peliculas, nuevaPelicula]);
            // Limpiar el estado de la nueva película
            setNuevaPelicula({ id: 0, titulo: "", genero: "", duracion: "", inventario: "" });
        }
    };

    // Función para eliminar una película
    const eliminarPelicula = (id) => {
        setPeliculas(peliculas.filter(pelicula => pelicula.id !== id));
    };

    // Función para actualizar una película
    const actualizarPelicula = (id, nuevaPelicula) => {
        setPeliculas(peliculas.map(pelicula => (pelicula.id === id ? nuevaPelicula : pelicula)));
    };

    // Manejar cambios en el formulario de nueva película
    const handleChange = (event) => {
        const { name, value } = event.target;
        setNuevaPelicula({ ...nuevaPelicula, [name]: value });
    };

    // Renderizar la lista de películas
    const listaPeliculas = peliculas.map(pelicula => (
        <div key={pelicula.id}>
            <p>{pelicula.titulo} - {pelicula.genero} ({pelicula.duracion} minutos) - Inventario: {pelicula.inventario}</p>
            <button onClick={() => eliminarPelicula(pelicula.id)}>Eliminar</button>
            {/* Agregar lógica para actualizar película */}
        </div>
    ));

    return (
        <div className="peliculas-container">
            <h2>CRUD de Películas</h2>
            {/* Formulario para agregar nuevas películas */}
            <form onSubmit={(e) => {
                e.preventDefault();
                agregarPelicula();
            }}>
                <input type="text" name="titulo" value={nuevaPelicula.titulo} onChange={handleChange} placeholder="Título de la película" />
                <input type="text" name="genero" value={nuevaPelicula.genero} onChange={handleChange} placeholder="Género" />
                <input type="number" name="duracion" value={nuevaPelicula.duracion} onChange={handleChange} placeholder="Duración (minutos)" />
                <input type="number" name="inventario" value={nuevaPelicula.inventario} onChange={handleChange} placeholder="Inventario" />
                <button type="submit">Agregar Película</button>
            </form>
            {/* Agregar lógica para editar película */}
            <div className="lista-peliculas">
                {listaPeliculas}
            </div>
        </div>
    );
};

export default CRUDPeliculas;
