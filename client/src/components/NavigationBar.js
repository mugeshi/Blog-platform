import React from 'react';
import { Link } from 'react-router-dom';

const NavigationBar = () => {
  return (
    <nav>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/blog">Blog Posts</Link></li>
      
      </ul>
    </nav>
  );
};

export default NavigationBar;
