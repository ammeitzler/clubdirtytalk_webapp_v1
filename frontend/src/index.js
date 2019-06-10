import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import './App.css';

import {
  Route,
  Link,
  BrowserRouter as Router
} from "react-router-dom";
import App from "./App";
import About from "./about";

const routing = (
  <Router>
    	<div className="main_menu">
			<ul>
				<li><Link to="/about">about</Link></li>
		        <li><Link to="/">search</Link></li>
				<li><Link to="/about">about</Link></li>
		        <li><Link to="/">search</Link></li>
				<li><Link to="/about">about</Link></li>
		        <li><Link to="/">search</Link></li>
				<li><Link to="/about">about</Link></li>
		        <li><Link to="/">search</Link></li>
				<li><Link to="/about">about</Link></li>
				<li><Link to="/">search</Link></li>
			</ul>
		</div>
      <Route exact path="/" component={App} />
      <Route path="/about" component={About} />
      	<div className="main_menu">
			<ul>
				<li><Link to="/about">about</Link></li>
		        <li><Link to="/">search</Link></li>
				<li><Link to="/about">about</Link></li>
		        <li><Link to="/">search</Link></li>
				<li><Link to="/about">about</Link></li>
		        <li><Link to="/">search</Link></li>
				<li><Link to="/about">about</Link></li>
		        <li><Link to="/">search</Link></li>
				<li><Link to="/about">about</Link></li>
				<li><Link to="/">search</Link></li>
			</ul>
		</div>
  </Router>
)

ReactDOM.render(routing, document.getElementById('root'))