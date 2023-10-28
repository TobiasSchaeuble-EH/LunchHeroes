import './App.css';
import Login from './Components/Login';  // import the Login component
import {useSelector} from 'react-redux';  // import useSelector from react-redux
import { Route, Navigate, Routes } from 'react-router-dom';  // import Route and Navigate from react-router-dom

function App() {
  let user;
  // const user = useSelector(state => state.session.user);
  return (
      <Routes>
        {user ? (
          //routes that will be available ONLY when user is logged in
          //add additional routes here
          <Route element={<Login />} path="/home" />
        ) : (
          //will redirect to '/' from any url if no user is logged in
          //do not add additional routes here
          <Route path="*" element={<Navigate to="/" replace />} />
        )}
        //login form will always be available //any route added here will always
        be available
        <Route element={<Login />} path="/" />
     </Routes>
  );
}

export default App;
