import React from 'react';
import PropTypes from 'prop-types';
import useStyles from './styles';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import {Link} from 'react-router-dom';

function ScriptsView(props) {
  const classes = useStyles();
  const {
    scripts
  } = props;
  
  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell variant='head'>ID</TableCell>
            <TableCell variant='head'>Название</TableCell>
            <TableCell variant='head'>Статус</TableCell>
            <TableCell variant='head'>Версия</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {scripts.map(({id, name, status, version}) => {
            return (
              <TableRow key={id} hover>
                <TableCell>{id}</TableCell>
                <TableCell><Link to={`/script/${id}`}>{name}</Link></TableCell>
                <TableCell>{status}</TableCell>
                <TableCell>{version}</TableCell>
              </TableRow>
            );
          })}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

ScriptsView.propTypes = {
  scripts: PropTypes.arrayOf(PropTypes.object).isRequired
};

export default ScriptsView;