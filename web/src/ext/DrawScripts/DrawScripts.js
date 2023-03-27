import React, {Component} from 'react';
import DrawScriptsView from './DrawScriptsView';
import {useParams, useNavigate} from 'react-router-dom';
import PropTypes from 'prop-types';

class DrawScripts extends Component {
  static propTypes = {
    scriptId: PropTypes.number,
    navigate: PropTypes.func
  };
  
  counterNodes = 0;
  
  constructor(props) {
    super(props);
    
    this.state = {
      script: undefined
    };
  }
  
  async componentDidUpdate(prevProps, prevState, snapshot) {
    if (prevProps.scriptId !== this.props.scriptId && this.props.scriptId) {
      const script = await this.loadScript(this.props.scriptId);
      
      if (script) {
        this.setState({script});
      }
    }
  }
  
  async componentDidMount() {
    if (this.props.scriptId) {
      const script = await this.loadScript(this.props.scriptId);
      
      if (script) {
        this.setState({script});
      }
    }
  }
  
  loadScript = async scriptId => {
    const requestOptions = {
        method: 'GET',
        headers: {'Content-Type': 'application/json'}
    };
    const response = await fetch(`/api/v1/script/${scriptId}`, requestOptions);
    
    if (response.status === 200) {
      return await response.json();
    }
  }
  
  generateId = () => {
    return `action_${+new Date()}_${this.counterNodes}`;
  };
  
  generateNewNode = (startAction = false) => ({
    id: this.generateId(),
    data: {
      label: `Действие ${++this.counterNodes}`,
      description: 'Содержание действия',
      countSources: 0,
      startAction,
      sources: []
    },
    type: 'action',
    position: {
      x: 10 + this.counterNodes * 20,
      y: 10 + this.counterNodes * 4
    }
  });
  
  generateScriptNode = () => ({
    id: 'script-card',
    data: {
      label: 'Название скрипта',
      description: 'Описание скрипта'
    },
    type: 'script',
    draggable: false,
    selectable: false,
    position: {
      x: 0,
      y: -250
    }
  });
  
  onSave = async data => {
    const {
      nodes,
      edges
    } = data;
    const {
      script
    } = this.state;
    const {
      id
    } = script || {};
    const cardIndex = nodes.findIndex(({id}) => id === 'script-card');
    let nameScript = '';
    let descScript = '';
    
    if (cardIndex !== -1) {
      const card = nodes[cardIndex];
      
      nameScript = card.data.label;
      descScript = card.data.description;
    }
    const requestOptions = {
      method: !!script ? 'PUT' : 'POST',
      body: JSON.stringify({
        name: nameScript,
        description: descScript,
        nodes: nodes.map(({id, data, position, type, handleBounds, draggable, selectable}) =>
          ({id, data, position, type, handleBounds, draggable, selectable})),
        edges: edges.map(({id, source, sourceHandle, target, targetHandle, type}) =>
          ({id, source, sourceHandle, target, targetHandle, type}))
      }),
      headers: {'Content-Type': 'application/json'}
    };
    const response = await fetch(`/api/v1/script${!!script ? `/${id}` : ''}`, requestOptions);
    const responseData = await response.json();
    
    if (response.status === 200 && !script) {
      this.props.navigate(`/script/${responseData.id}`, {replace: true});
    }
  };
  
  render() {
    const {
      script
    } = this.state;
    const {
      scriptId
    } = this.props;
    let nodes = [
      this.generateScriptNode(),
      this.generateNewNode(true)
    ];
    let edges = [];
    
    if (!script && scriptId) {
      return;
    } else if (script && scriptId) {
      nodes = script.nodes;
      edges = script.edges;
    }
    return (
      <DrawScriptsView nodes={nodes}
                       edges={edges}
                       onSave={this.onSave}
                       generateNewNode={this.generateNewNode}/>
    );
  }
}

export default (WrappedComponent => (props => {
  let {
    script_id: scriptId
  } = useParams();
  
  if (scriptId) {
    scriptId = parseInt(scriptId);
  }
  return <WrappedComponent {...props} scriptId={scriptId} navigate={useNavigate()}/>
}))(DrawScripts);
