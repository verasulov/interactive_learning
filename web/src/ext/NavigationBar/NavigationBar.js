import React, {Component} from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import {Link as NavLink} from 'react-router-dom';
import settings from './settings.json';

class NavigationBar extends Component {
  render() {
    return (
        <AppBar position='static'>
          <Toolbar>
            <Typography variant='h6' component='div'>
              Интерактивные обучения
            </Typography>
            <Typography variant='body1' style={{marginLeft: '15px'}}>
              <NavLink to='/scripts' style={{color: '#fff'}}>Скрипты</NavLink>
            </Typography>
            <Link variant='body1'
                  underline='hover'
                  color='#fff'
                  style={{marginLeft: 'auto'}}
                  href='/oauth2/logout'>
              Выйти
            </Link>
          </Toolbar>
        </AppBar>
    );
  }
}

export default NavigationBar;