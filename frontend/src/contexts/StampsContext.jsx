import React, { createContext, useState, useContext, useEffect } from 'react';

const StampsContext = createContext();

export const StampsProvider = ({ children }) => {
  const [stamps, setStamps] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchStamps = async () => {
    try {
      setLoading(true);
      const response = await fetch('http://localhost:5000/api/stamps');
      if (!response.ok) {
        throw new Error('Failed to fetch stamps');
      }
      const data = await response.json();
      setStamps(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchStamps();
  }, []);

  return (
    <StampsContext.Provider value={{ stamps, loading, error, fetchStamps }}>
      {children}
    </StampsContext.Provider>
  );
};

export const useStamps = () => useContext(StampsContext);