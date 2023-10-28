import React, { useState } from 'react';
// import logo from './logo.svg';
import './App.css';
import Login from './Components/Login';
import Navigation from './Components/Navigation';
import { useNavigate, useDispatch } from "react-router-dom";
import Profile from './Components/Profile';
import Status from './Components/Status';
import {useSelector} from 'react-redux';  // import useSelector from react-redux
import { Route, Navigate, Routes } from 'react-router-dom';  // import Route and Navigate from react-router-dom

function App() {
  // const [isLoaded, setIsLoaded] = useState(false);
  // useEffect(() => {
  //   dispatch(authenticate()).then(() => setIsLoaded(true));
  // }, [dispatch]);

  const props = {
    name: "John Doe",
    email: "johndoe@example.com",
    location: "New York, USA",
    department: "Engineering",
    groupSize: 2,
    // profilePicture: "./profile.png",
    timeSlot: "10:00",
    interests: ["Coding", "Traveling", "Reading"],
    isScheduled: true
  };

  const [groupSize, setGroupSize] = useState(props.groupSize);
  const [timeSlot, setTimeSlot] = useState(props.timeSlot);

  const handleGroupSizeChange = (size) => {
    setGroupSize(size);
  }

  const handleTimeSlotChange = (slot) => {
    setTimeSlot(slot);
  }

  const user = useSelector(state => state.session.user);

  const Wrapper = () => {
    return (
        <p>
        </p>
        <a
          name={props.name}
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
          onGroupSizeChange={handleGroupSizeChange} // Changed from props.onGroupSizeChange
          onTimeSlotChange={handleTimeSlotChange}   // Changed from props.onTimeSlotChange
        </a>
      </header>
        <Status isScheduled={!props.isScheduled} />
    );
  }

  console.log(user);
  return (
    <>
      <Navigation /*isLoaded={isLoaded}*/ />
      <Routes>
        <Route element={
          <Wrapper
          />
        } path="/" />
        {/* {user ? (
          //routes that will be available ONLY when user is logged in
          //add additional routes here
          <Route element={<Profile />} path="/home" />
        ) : (
          //will redirect to '/' from any url if no user is logged in
          //do not add additional routes here
          <Route path="*" element={<Navigate to="/" replace />} />
        )}
        <Route element={<Login />} path="/" /> */}
      </Routes>
    </>
  );
}

export default App;
