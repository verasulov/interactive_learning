import React, {Component} from 'react';
import ScriptsView from './ScriptsView';

class Scripts extends Component {
  constructor(props) {
    super(props);
    
    this.state = {
      scripts: []
    };
  }
  
  async componentDidMount() {
    const scripts = await this.loadScripts();
    
    if (scripts) {
      this.setState({scripts});
    }
  }
  
  loadScripts = async () => {
    const filter = JSON.stringify([]);
    const options = JSON.stringify({});
    const requestOptions = {
        method: 'GET',
        headers: {'Content-Type': 'application/json'}
    };
    const response = await fetch(`/api/v1/scripts?filter=${filter}&options=${options}`, requestOptions);
    
    if (response.status === 200) {
      return await response.json();
    }
  }
  
  render() {
    const {
      scripts
    } = this.state;
    
    return (
      <ScriptsView scripts={scripts}/>
    );
  }
}

export default Scripts;
