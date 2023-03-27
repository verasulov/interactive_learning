import {makeStyles, createStyles} from '@mui/styles';

export default makeStyles(() =>
  createStyles({
    controls: {
      position: 'absolute',
      zIndex: 5,
      top: 15,
      left: 15
    },
    scriptNode: {
      minWidth: '300px',
      border: '1px solid #eee',
      padding: '15px 5px',
      borderRadius: '5px',
      background: '#d3e5f7',
      pointerEvents: 'auto'
    },
    actionNode: {
      minWidth: '300px',
      border: '1px solid #eee',
      padding: '15px 5px',
      borderRadius: '5px',
      background: 'white'
    },
    actionCheckBox: {
      marginLeft: '10px !important'
    },
    sourceContainer: {
      position: 'relative',
      marginBottom: '15px',
      marginTop: '10px'
    },
    sourcePoint: {
      left: '102%',
      top: '46%',
      height: '10px',
      width: '10px'
    },
    targetPoint: {
      height: '10px',
      width: '10px'
    },
    descriptionNode: {
      marginTop: '15px !important',
      marginBottom: '15px !important'
    }
  })
);
