import React, { useState } from 'react';
import './CRUDRentas.css';

const CRUDRentas = () => {
    // Estado para almacenar la lista de rentas
    const [rentas, setRentas] = useState([]);
    // Estado para la nueva renta a agregar
    const [nuevaRenta, setNuevaRenta] = useState({
        id: "",
        idCliente: "",
        idPelicula: "",
        fecha: "",
        estatus: "",
        diasRentado: ""
    });

    // Función para agregar una nueva renta
    const agregarRenta = () => {
        if (nuevaRenta.idCliente.trim() !== "" && nuevaRenta.idPelicula.trim() !== "" && nuevaRenta.fecha.trim() !== "" && nuevaRenta.estatus.trim() !== "" && nuevaRenta.diasRentado.trim() !== "") {
            setRentas([...rentas, nuevaRenta]);
            // Limpiar el estado de la nueva renta
            setNuevaRenta({ id: "", idCliente: "", idPelicula: "", fecha: "", estatus: "", diasRentado: "" });
        }
    };

    // Función para eliminar una renta
    const eliminarRenta = (id) => {
        setRentas(rentas.filter(renta => renta.id !== id));
    };

    // Manejar cambios en el formulario de nueva renta
    const handleChange = (event) => {
        const { name, value } = event.target;
        setNuevaRenta({ ...nuevaRenta, [name]: value });
    };

    // Renderizar la lista de rentas
    const listaRentas = rentas.map(renta => (
        <div key={renta.id}>
            <p>Renta ID: {renta.id}</p>
            <p>Cliente ID: {renta.idCliente}</p>
            <p>Película ID: {renta.idPelicula}</p>
            <p>Fecha: {renta.fecha}</p>
            <p>Estatus: {renta.estatus}</p>
            <p>Días Rentado: {renta.diasRentado}</p>
            <button onClick={() => eliminarRenta(renta.id)}>Eliminar</button>
            {/* Agregar lógica para actualizar renta */}
        </div>
    ));

    return (
        <div className="rentas-container">
            <h2>CRU de Rentas</h2>
            {/* Formulario para agregar nuevas rentas */}
            <form onSubmit={(e) => {
                e.preventDefault();
                agregarRenta();
            }}>
                <input type="text" name="idCliente" value={nuevaRenta.idCliente} onChange={handleChange} placeholder="ID del cliente" />
                <input type="text" name="idPelicula" value={nuevaRenta.idPelicula} onChange={handleChange} placeholder="ID de la película" />
                <input type="date" name="fecha" value={nuevaRenta.fecha} onChange={handleChange} />
                <input type="text" name="estatus" value={nuevaRenta.estatus} onChange={handleChange} placeholder="Estatus" />
                <input type="text" name="diasRentado" value={nuevaRenta.diasRentado} onChange={handleChange} placeholder="Días Rentado" />
                <button type="submit">Agregar Renta</button>
            </form>
            {/* Agregar lógica para editar renta */}
            <div className="lista-rentas">
                {listaRentas}
            </div>
        </div>
    );
};

export default CRUDRentas;
