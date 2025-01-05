import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

const StampDetail = () => {
  const { id } = useParams(); // Pobranie ID z adresu URL
  const [stamp, setStamp] = useState(null); // Dane szczegółowe znaczka
  const [loading, setLoading] = useState(true); // Status ładowania
  const [error, setError] = useState(null); // Obsługa błędów

  useEffect(() => {
    const fetchStamp = async () => {
      try {
        const response = await fetch(`http://localhost:5000/api/stamps/${id}`);
        if (!response.ok) {
          throw new Error(`Błąd HTTP: ${response.status}`);
        }
        const data = await response.json();
        setStamp(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchStamp();
  }, [id]);

  if (loading) {
    return <div className="text-center py-8">Ładowanie...</div>;
  }

  if (error) {
    return <div className="text-center text-red-500 py-8">Błąd: {error}</div>;
  }

  if (!stamp) {
    return <div className="text-center py-8">Nie znaleziono znaczka</div>;
  }

  return (
    <div className="stamp-detail-container">
      <h1 className="stamp-name">{stamp.name}</h1>
      <img
        src={stamp.image_url}
        alt={stamp.name}
        className="stamp-image"
        style={{ width: '100%', maxHeight: '300px', objectFit: 'contain' }}
      />
      <p>{stamp.description}</p>
      <p>
        <strong>Kraj:</strong> {stamp.country}
      </p>
      <p>
        <strong>Rok wydania:</strong> {stamp.year_issued}
      </p>
      <p>
        <strong>Cena:</strong> {stamp.price} zł
      </p>
      <p>
        <strong>Ilość dostępna:</strong> {stamp.quantity_available}
      </p>
      <p>
        <strong>Średnia ocena:</strong> {stamp.average_rating} (na podstawie {stamp.reviews_count} recenzji)
      </p>
    </div>
  );
};

export default StampDetail;
