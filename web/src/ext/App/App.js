import React, {Component} from 'react';
import NavigationBar from '../NavigationBar';
import DrawScripts from '../DrawScripts';
import Scripts from '../Scripts';
import Box from '@mui/material/Box';
import {
  BrowserRouter,
  Route,
  Routes
} from 'react-router-dom';


class App extends Component {
  render() {
    return(
      <React.Fragment>
        <BrowserRouter>
          <NavigationBar/>
          <Box style={{height: 'calc(100% - 64px)'}}>
              <Routes>
                <Route path='/script' element={<DrawScripts/>}>
                  <Route path=':script_id' element={<DrawScripts/>}/>
                </Route>
                <Route path='/scripts' element={<Scripts/>}/>
              </Routes>
          </Box>
        </BrowserRouter>
      </React.Fragment>
    );
  }
}

export default App;