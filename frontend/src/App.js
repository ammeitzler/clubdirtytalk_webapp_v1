import React, { Component } from 'react';


const url = 'http://18.216.255.48:8000/article/'

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
      value:'Club Dirty Talk',
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
    this.setState({value: this.state.value});
    event.preventDefault();
  }

  render() {
    return (
      <div id="home_pg">
          <div id="twothird">
            <SearchResults state={this.state}/>
          </div>
          <div id="onethird">
            <form  onSubmit={this.handleSubmit} id="main_search">
              <label>
                <textarea value={this.state.value} onChange={this.handleChange} autoFocus/>
              </label>
              <input id="submit_button" type="submit" value="search" />
            </form>
          </div>
      </div>
    );
  }
}

export default App;