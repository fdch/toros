import { useState, useEffect } from "react";
import './About.css'

function About() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("/people")
      .then(res => res.json())
      .then(data => setData(data));
  }, []);
  
  return (
    <div> 
      <h2>About</h2>
    {!data ? "Loading...": data.map((obj, index) => {
        return(
          <div key={index}>
            <h3>{obj.name}</h3>
            <div>{obj.bio.en.long.map((par, idx) => <p key={idx}>{par}</p>)}</div>
          </div>
        )
      })
     }
  </div> 
  );
}

export default About;
