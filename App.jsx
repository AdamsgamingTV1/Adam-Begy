import React, { useState, useEffect } from 'react';
import './App.css';

const ThemeToggleButton = ({ theme, toggleTheme }) => {
    return (
        <button onClick={toggleTheme}>
            {theme == 'light' ? 'Přepnout na tmavé' : 'Přepnout na světlé'}
        </button>

    );
};

const App = () => {
    const [ theme, setTheme ] = useState (() => {
        const savedTheme = localStorage.getItem('theme');
        return savedTheme || 'light';
    });

    useEffect(() => {
        logalStorage.setItem('theme', theme);
    }, [theme]);

    const toggleTheme = () => {
        setTheme(prevTheme => (prevTheme === 'light' ? 'dark' : 'light'));
    };

    return (
    <div className={`app ${theme}`}>
      {/* Navigační panel */}
      <nav>
        <h1>Můj web</h1>
      </nav>

      {/* Obsah stránky */}
      <main>
        <h2>Vítejte na mé stránce</h2>
        <p>Tady bude váš obsah...</p>
      </main>

      {/* Tlačítko pro přepínání tématu */}
      <ThemeToggleButton theme={theme} toggleTheme={toggleTheme} />

      {/* Patička */}
      <footer>
        <p>&copy; 2024 Můj web</p>
      </footer>
    </div>
  );
};

export default App;