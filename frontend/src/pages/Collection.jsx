import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import '../styles/main.css';

const Collection = () => {
  const [stamps, setStamps] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/stamps')
      .then((response) => {
        if (!response.ok) {
          console.error(`Server returned ${response.status}: ${response.statusText}`);
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Fetched data:', data);
        setStamps(data.stamps); // Adjust based on backend response structure
      })
      .catch((error) => console.error('Error fetching stamps:', error));
  }, []);

  return (
    <div className="collection">
      <h1 className="collection-title">Kolekcja znaczków</h1>
      {stamps && stamps.length > 0 ? (
        <div className="collection-grid">
          {stamps.map((stamp) => (
            <div key={stamp.id} className="collection-item">
              <Link to={`/stamps/${stamp.id}`} className="collection-item-link">
                <img
                  src={stamp.image_url}
                  alt={stamp.name}
                  className="collection-item-image"
                />
              </Link>
              <h3 className="collection-item-name">{stamp.name}</h3>
              <p className="collection-item-description">{stamp.description}</p>
              <p className="collection-item-price">{stamp.price} zł</p>
              <Link to={`/stamps/${stamp.id}`} className="collection-item-link">
                Więcej informacji
              </Link>
            </div>
          ))}
        </div>
      ) : (
        <p className="collection-empty">Nie znaleziono znaczków</p>
      )}
    </div>
  );
};

export default Collection;
