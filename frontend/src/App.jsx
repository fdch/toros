import { useState } from "react";
import './About.css'
import About from './About';
import Events from './About';
import Works from './About';
import Contact from './About';

function App() {
  const [page, setPage] = useState(null);
  const useAbout = () => {
    console.log('Using About');
    setPage('about');
  };
  const useEvents = () => {
    console.log('Using Events');
    setPage('events');
  };
  const useWorks = () => {
    console.log('Using Works');
    setPage('works');
  };
  const useContact = () => {
    console.log('Using Contact');
    setPage('contact');
  };

  return (
    <div className="App">
      <header className="App-header">

          <h1>TOROS</h1>
          <h2>EXPERIMENTAL MUSIC DUO</h2>
       
      
      <nav>
        <button onClick={useAbout}>About</button>
        <button onClick={useEvents}>Events</button>
        <button onClick={useWorks}>Works</button>
        <button onClick={useContact}>Contact</button>
      </nav>
      </header>
	<main>
	    {
         page==='about' ? <About/> 
        : page==='events'? <Events/> 
        : page==='works'? <Works/>
        : page==='contact'? <Contact/>
        : null
	    }
      </main>
    </div>
  );
}

export default App;
