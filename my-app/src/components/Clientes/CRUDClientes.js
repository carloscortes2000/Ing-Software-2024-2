import React, { useState } from 'react';
import './CRUDClientes.css';

const CRUDClientes = () => {
    // Estado para almacenar la lista de clientes
    const [clientes, setClientes] = useState([]);
    // Estado para el nuevo cliente a agregar
    const [nuevoCliente, setNuevoCliente] = useState({
        id: "",
        nombre: "",
        apellidoPaterno: "",
        apellidoMaterno: "",
        email: "",
        contraseña: "",
        fotodePerfil: "",
        superUsuario: false
    });

    // Función para agregar un nuevo cliente
    const agregarCliente = () => {
        if (nuevoCliente.nombre.trim() !== "" && nuevoCliente.email.trim() !== "" && nuevoCliente.contraseña.trim() !== "") {
            setClientes([...clientes, nuevoCliente]);
            // Limpiar el estado del nuevo cliente
            setNuevoCliente({ 
                id: "", 
                nombre: "", 
                apellidoPaterno: "", 
                apellidoMaterno: "", 
                email: "", 
                contraseña: "", 
                fotodePerfil: "", 
                superUsuario: false 
            });
        }
    };

    // Función para eliminar un cliente
    const eliminarCliente = (id) => {
        setClientes(clientes.filter(cliente => cliente.id !== id));
    };

    // Manejar cambios en el formulario de nuevo cliente
    const handleChange = (event) => {
        const { name, value, type, checked } = event.target;
        const newValue = type === 'checkbox' ? checked : value;
        setNuevoCliente({ ...nuevoCliente, [name]: newValue });
    };

    // Renderizar la lista de clientes
    const listaClientes = clientes.map(cliente => (
        <div key={cliente.id}>
            <p>{cliente.nombre}</p>
            <button onClick={() => eliminarCliente(cliente.id)}>Eliminar</button>
            {/* Agregar lógica para actualizar cliente */}
        </div>
    ));

    return (
        <div className="clientes-container">
            <h2>CRUD de Clientes</h2>
            {/* Formulario para agregar nuevos clientes */}
            <form onSubmit={(e) => {
                e.preventDefault();
                agregarCliente();
            }}>
                <input type="text" name="nombre" value={nuevoCliente.nombre} onChange={handleChange} placeholder="Nombre del cliente" />
                <input type="text" name="apellidoPaterno" value={nuevoCliente.apellidoPaterno} onChange={handleChange} placeholder="Apellido Paterno" />
                <input type="text" name="apellidoMaterno" value={nuevoCliente.apellidoMaterno} onChange={handleChange} placeholder="Apellido Materno" />
                <input type="email" name="email" value={nuevoCliente.email} onChange={handleChange} placeholder="Correo Electrónico" />
                <input type="password" name="contraseña" value={nuevoCliente.contraseña} onChange={handleChange} placeholder="Contraseña" />
                <input type="text" name="fotodePerfil" value={nuevoCliente.fotodePerfil} onChange={handleChange} placeholder="URL de Foto de Perfil" />
                <label>
                    <input type="checkbox" name="superUsuario" checked={nuevoCliente.superUsuario} onChange={handleChange} />
                    Es Super Usuario
                </label>
                <button type="submit">Agregar Cliente</button>
            </form>
            {/* Agregar lógica para editar cliente */}
            <div className="lista-clientes">
                {listaClientes}
            </div>
        </div>
    );
};

export default CRUDClientes;
