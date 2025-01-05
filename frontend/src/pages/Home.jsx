import { Link } from 'react-router-dom';
import { useStamps } from '../contexts/StampsContext';
import { StampCard } from '../components/StampCard';

const Home = () => {
  const { stamps, loading } = useStamps();
  const featuredStamps = Array.isArray(stamps) ? stamps.slice(0, 3) : []; // Display first 3 stamps as featured

  return (
    <div className="home">
      <div className="home-header">
        <h1 className="home-title">Sklep Filatelistyczny</h1>
        <p className="home-subtitle">
          Odkryj naszą wyjątkową kolekcję znaczków pocztowych
        </p>
      </div>

      <div className="home-banner">
        <h2 className="home-banner-title">Witamy w naszym sklepie</h2>
        <p className="home-banner-text">Znajdź znaczki, których szukasz w naszej bogatej kolekcji</p>
        <Link to="/collection" className="home-banner-button">
          Zobacz kolekcję
        </Link>
      </div>

      <div className="home-featured">
        <h2 className="home-featured-title">Wyróżnione znaczki</h2>
        {loading ? (
          <div className="home-loading">Ładowanie...</div>
        ) : (
          <div className="home-stamps">
            {featuredStamps.map((stamp) => (
              <StampCard key={stamp.id} stamp={stamp} />
            ))}
          </div>
        )}
      </div>
    </div>

  );
};

export default Home;