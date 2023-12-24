import React from 'react';
import { Switch, Route } from 'react-router-dom';
import Home from './Home';
import BlogPosts from '.components/BlogPosts'; 
const Routes = () => {
  return (
    <Switch>
      <Route exact path="/" component={Home} />
      <Route path="/blog" component={BlogPosts} />
     
    </Switch>
  );
};

export default Routes;
