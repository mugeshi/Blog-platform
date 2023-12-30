import React from 'react';
//import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router } from 'react-router-dom';
import CustomRoutes from './routes';
import NavigationBar from './NavigationBar';
import BlogPostList from './BlogPost';

const App = () => {
  return (
    <Router>
      <div>
        <NavigationBar />
        <CustomRoutes />
        <BlogPostList />
      </div>
    </Router>
  );
};

//const root = document.getElementById('root');
//const appRoot = createRoot(root);
//appRoot.render(<App />);

export default App;