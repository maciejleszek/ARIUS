import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import { useCart } from '../contexts/CartContext';

const StampCard = ({ stamp }) => {
  const { addToCart } = useCart();

  return (
    <div className="bg-white rounded-lg shadow-md p-4">
      <img
        src={stamp.imageUrl}
        alt={stamp.name}
        className="w-full h-48 object-contain mb-4"
      />
      <h3 className="text-lg font-semibold">{stamp.name}</h3>
      <p className="text-gray-600 text-sm mb-2">{stamp.description}</p>
      <div className="text-sm text-gray-500 mb-2">
        <p>Wymiary: {stamp.dimensions}</p>
        <p>Stan: {stamp.condition}</p>
      </div>
      <div className="mt-4 flex justify-between items-center">
        <span className="text-xl font-bold">{stamp.price} zł</span>
        <div className="space-x-2">
          <Link
            to={`/stamp/${stamp.id}`}
            className="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600"
          >
            Szczegóły
          </Link>
          <button
            onClick={() => addToCart(stamp)}
            className="bg-green-500 text-white px-3 py-1 rounded hover:bg-green-600"
          >
            Do koszyka
          </button>
        </div>
      </div>
    </div>
)}

StampCard.propTypes = {
  stamp: PropTypes.shape({
    imageUrl: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    dimensions: PropTypes.string.isRequired,
    condition: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    id: PropTypes.string.isRequired,
  }).isRequired,
};

export default StampCard;export { StampCard };