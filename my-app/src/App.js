import React from 'react';
import './App.css';
import CRUDClientes from './components/Clientes/CRUDClientes';
import CRUDPeliculas from './components/Peliculas/CRUDPeliculas';
import CRUDRentas from './components/Rentas/CRUDRentas';

function App() {
  return (
    <div className="app">
      <h1>Bienvenido a la aplicación de gestión de rentas de películas</h1>
      <CRUDClientes />
      <CRUDPeliculas />
      <CRUDRentas />
    </div>
  );
}

export default App;
