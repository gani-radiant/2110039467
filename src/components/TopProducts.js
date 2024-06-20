// src/components/TopProducts.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TopProducts = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProducts = async () => {
      setLoading(true);
      setError(null);

      try {
        const response = await axios.get(
          'http://20.244.56.144/test/companies/AMZ/categories/Laptop/products',
          {
            params: {
              top: 10,
              minPrice: 1,
              maxPrice: 10000
            }
          }
        );

        setProducts(response.data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h1>Top Products</h1>
      <ul>
        {products.map((product, index) => (
          <li key={index}>
            <p>Product Name: {product.productName}</p>
            <p>Price: {product.price}</p>
            <p>Rating: {product.rating}</p>
            <p>Discount: {product.discount}</p>
            <p>Availability: {product.availability}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TopProducts;
