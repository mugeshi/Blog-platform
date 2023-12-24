import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Routes from './components/Routes';
import NavigationBar from './components/NavigationBar';
import BlogPostList from './components/BlogPostList';

const App = () => {
  return (
    <Router>
      <div>
        <NavigationBar />
        <Switch>
          <Route exact path="/" component={Routes} />
          <Route path="/blog" component={BlogPostList} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;
