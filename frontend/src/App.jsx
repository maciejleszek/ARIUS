import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import { CartProvider } from './contexts/CartContext';
import { StampsProvider } from './contexts/StampsContext';
import Navigation from './components/Navigation';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Collection from './pages/Collection';
import StampDetail from './pages/StampDetail';
import Cart from './pages/Cart';
import Checkout from './pages/Checkout';
import Profile from './pages/Profile';
import './styles/main.css';

const App = () => {
  return (
    <AuthProvider>
      <StampsProvider>
        <CartProvider>
          <Router>
            <div className="min-h-screen bg-gray-100">
              <Navigation />
              <div className="container mx-auto px-4 py-8">
                <Routes>
                  <Route path="/" element={<Home />} />
                  <Route path="/login" element={<Login />} />
                  <Route path="/register" element={<Register />} />
                  <Route path="/collection" element={<Collection />} />
                  <Route path="/stamps/:id" element={<StampDetail />} />
                  <Route path="/cart" element={<Cart />} />
                  <Route path="/checkout" element={<Checkout />} />
                  <Route path="/profile" element={<Profile />} />
                </Routes>
              </div>
            </div>
          </Router>
        </CartProvider>
      </StampsProvider>
    </AuthProvider>
  );
};

export default App;