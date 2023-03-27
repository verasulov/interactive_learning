import React, {useState, useCallback} from 'react';
import ReactFlow, {
  Background,
  MiniMap,
  Controls,
  useNodesState,
  useEdgesState,
  addEdge
} from 'react-flow-renderer';
import PropTypes from 'prop-types';
import useStyles from './styles';
import ButtonGroup from '@mui/material/ButtonGroup';
import Button from '@mui/material/Button';
import ActionNode from './ActionNode';
import ScriptNode from './ScriptNode';

const nodeTypes = {
  action: ActionNode,
  script: ScriptNode
};

function DrawScriptsView(props) {
  const classes = useStyles();
  const {
    nodes: initialNodes,
    edges: initialEdges,
    generateNewNode,
    onSave
  } = props;
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
  const onConnect = useCallback((connection) => {
    setEdges((eds) => addEdge(connection, eds));
  }, []);
  const onAdd = useCallback(() => {
    const newNode = {
      position: {
        x: Math.random() * window.innerWidth - 100,
        y: Math.random() * window.innerHeight,
      },
      ...(generateNewNode())
    };
    
    setNodes((nds) => nds.concat(newNode));
  }, [setNodes]);
  const [rfInstance, setRfInstance] = useState(null);
  const onClickSave = useCallback(() => {
    if (!rfInstance) {
      console.error('variable rfInstance not found');
      return;
    }
    onSave(rfInstance.toObject());
  }, [rfInstance]);
  
  return (
    <ReactFlow nodes={nodes}
               edges={edges}
               onNodesChange={onNodesChange}
               onEdgesChange={onEdgesChange}
               onConnect={onConnect}
               onInit={setRfInstance}
               nodeTypes={nodeTypes}
               defaultEdgeOptions={{type: 'simplebezier'}}
               fitView>
      <ButtonGroup className={classes.controls}>
        <Button onClick={onClickSave}>Сохранить</Button>
        <Button onClick={onAdd}>Добавить действие</Button>
      </ButtonGroup>
      <Background variant='lines'/>
      <Controls/>
      <MiniMap/>
    </ReactFlow>
  );
}

DrawScriptsView.propTypes = {
  nodes: PropTypes.arrayOf(PropTypes.object).isRequired,
  edges: PropTypes.arrayOf(PropTypes.object).isRequired,
  generateNewNode: PropTypes.func.isRequired,
  onSave: PropTypes.func.isRequired,
};

export default DrawScriptsView;