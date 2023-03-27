import React, {useCallback} from 'react';
import useStyles from './styles';
import TextField from '@mui/material/TextField';


function ScriptNode(node) {
  const {
    data: {
      label,
      description
    }
  } = node;
  const classes = useStyles();
  const onChangeLabel = useCallback(event => {
    node.data.label = event.target.value;
  }, [node]);
  const onChangeDescription = useCallback(event => {
    node.data.description = event.target.value;
  }, [node]);
  
  return (
    <div className={classes.scriptNode}>
      <TextField label='Название'
                 fullWidth
                 defaultValue={label}
                 onChange={event => onChangeLabel(event)}/>
      <TextField label={'Описание'}
                 defaultValue={description}
                 fullWidth
                 multiline
                 className={classes.descriptionNode}
                 minRows={2}
                 maxRows={6}
                 onChange={event => onChangeDescription(event)}/>
    </div>
  );
}

export default ScriptNode;
