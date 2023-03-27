import React, {useCallback, useState} from 'react';
import {Handle, Position} from 'react-flow-renderer';
import useStyles from './styles';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';


function ActionNode(node) {
  const {
    data: {
      label,
      description,
      startAction: defaultStartAction,
      countSources: defaultCountSources,
      sources
    }
  } = node;
  const [stateActionData, setStateActionData] = useState({
    startAction: defaultStartAction,
    countSources: defaultCountSources
  });
  const {
    startAction,
    countSources
  } = stateActionData;
  const classes = useStyles();
  const onChangeLabel = useCallback(event => {
    node.data.label = event.target.value;
  }, [node]);
  const onChangeDescription = useCallback(event => {
    node.data.description = event.target.value;
  }, [node]);
  const onChangeActionStart = useCallback(event => {
    node.data.startAction = event.target.checked;
    setStateActionData({...stateActionData, startAction: node.data.startAction});
  }, [setStateActionData, stateActionData, node]);
  const onClickAddSource = useCallback(() => {
    node.data.countSources += 1;
    setStateActionData({...stateActionData, countSources: node.data.countSources});
  }, [setStateActionData, stateActionData, node]);
  const onClickDeleteSource = useCallback(() => {
    node.data.countSources -= 1;
    setStateActionData({...stateActionData, countSources: node.data.countSources});
  }, [setStateActionData, stateActionData, node]);
  const sourcesBlock = [];
  
  for (let i = 0; i < countSources; i++) {
    if (sources[i] === undefined) {
      node.data.sources.push({
        sourceId: `${node.id}-${i}`,
        content: `Содержание варианта ${i+1}`
      });
    }
    const {
      sourceId,
      content
    } = node.data.sources[i];
    
    sourcesBlock.push(
      <Grid key={`source-${node.id}-${i}`} className={classes.sourceContainer}>
        <TextField label={`Вариант ${i+1}`}
                   defaultValue={content}
                   onChange={event => node.data.sources[i]['content'] = event.target.value}
                   fullWidth
                   multiline
                   rows={2}
                   size='small'/>
        <Handle type='source'
                id={sourceId}
                className={classes.sourcePoint}
                position={Position.Bottom} />
      </Grid>
    );
  }
  return (
    <div className={classes.actionNode}>
      {
        startAction ? null :
          <Handle type='target' id={`target-${node.id}`} position={Position.Left} className={classes.targetPoint}/>
      }
      <Grid>
        <TextField label='Название'
                   defaultValue={label}
                   size='small'
                   onChange={event => onChangeLabel(event)}/>
        <FormControlLabel checked={startAction}
                          className={classes.actionCheckBox}
                          label='Начало'
                          control={
                            <Checkbox size='small' onChange={event => onChangeActionStart(event)}/>
                          }/>
      </Grid>
      <TextField label={'Действие'}
                 defaultValue={description}
                 fullWidth
                 multiline
                 rows={2}
                 className={classes.descriptionNode}
                 size='small'
                 onChange={event => onChangeDescription(event)}/>
      <Grid>
        <Button size='small' onClick={() => onClickAddSource()}>Добавить вариант</Button>
        {
          node.data.countSources === 0 ? null :
            <Button size='small' onClick={() => onClickDeleteSource()}>Удалить вариант</Button>
        }
      </Grid>
      {sourcesBlock}
    </div>
  );
}

export default ActionNode;
