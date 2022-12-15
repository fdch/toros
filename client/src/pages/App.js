import { useState, useEffect } from "react";
import logo from '../images/logo.svg';
import Landing from './Landing.js';
import './App.css';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("/api")
      .then(res => res.json())
      .then(data => setData(data.message));
  }, []);
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
	  {!data ? "Loading..." : <Landing/>}
        </p>
        
      </header>
    </div>
  );
}

export default App;
