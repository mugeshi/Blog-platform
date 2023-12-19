import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import Routes from './Routes';
import NavigationBar from './components/NavigationBar';

const App = () => {
  return (
    <Router>
      <div>
        <NavigationBar />
        <Routes />
      </div>
    </Router>
  );
};

export default App;
