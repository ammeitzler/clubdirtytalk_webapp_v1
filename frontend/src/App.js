import React, { Component } from 'react';
import './App.css';
// import logo from './logo.svg';

const url = 'http://localhost:8000/article/'

class Menu extends Component {
  render() {
    return (
      <div className="main_menu">
        <ul>
          <li>about</li>
          <li>inspo</li>
          <li>search</li>
          <li>about</li>
          <li>inspo</li>
          <li>search</li>
          <li>about</li>
          <li>inspo</li>
          <li>search</li>
          <li>about</li>
          <li>inspo</li>
          <li>search</li>
          <li>about</li>
          <li>inspo</li>
          <li>search</li>
        </ul>
      </div>
    );
  }
}


class SearchResults extends Component {
  render() {
    console.log(this.props.state)
    return (
      this.props.state.data.map(item => (
        <div key={item.title} className="video_container">
          <p>{item.title}</p>
          <a target="_blank" rel="noopener noreferrer" href={item.site_url}><img src={item.image_url} alt={item.title}/></a>
        </div>
      ))
    );
  }
}




class App extends Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.state = {
      value:'Convo Club',
      data:[]
    };
  }

  async componentDidMount() {
    try {
      const res = await fetch(url);
      const data = await res.json();
      this.setState({
        data
      });
      console.log(this.state)

    } catch (e) {
      console.log(e);
    }
  }

  async search_db(event) {
      try {
        const res = await fetch(url + event.target.value +'/');
        const data = await res.json();
        console.log(data)
        this.setState({
          data
        });
    } catch (e) {
      console.log(e);
    }
  }

  handleChange(event) {
    this.setState({value: event.target.value});
    console.log({value: event.target.value})
    this.search_db(event)
  }
  handleSubmit(event) {
    alert('A search was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <div id="main_content">
        <Menu />
          <div id="twothird">
            <SearchResults state={this.state}/>
          </div>
          <div id="onethird">
            <form id="main_search">
              <label>
                <textarea value={this.state.value} onChange={this.handleChange} autoFocus/>
              </label>
              <input type="submit" value="Submit" />
            </form>
          </div>
        <Menu />
      </div>
    );
  }
}

export default App;





