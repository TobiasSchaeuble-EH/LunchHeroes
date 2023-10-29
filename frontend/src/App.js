import React, { useState, useEffect} from 'react';
// import logo from './logo.svg';
import './App.css';
import Login from './Components/Login';
import Navigation from './Components/Navigation';
// import { useNavigate, useDispatch } from "react-router-dom";
import Profile from './Components/Profile';
import Status from './Components/Status';
import {useSelector} from 'react-redux';  // import useSelector from react-redux
import { Route, Navigate, Routes, useNavigate } from 'react-router-dom';  // import Route and Navigate from react-router-dom
import Scheduling from './Components/Scheduling';
// import{ supabase } from './supabaseclient';

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
  console.log("LOGIN USER", user?.user?.id);
  console.log("LOGIN", user);

  const RedirectToHome = () => {
    const navigate = useNavigate();
  
    useEffect(() => {
      navigate('/home');
    }, [navigate]);
  
    return null; // This component does not render anything to the DOM
  }

  const Wrapper = () => {
    return (
      <div>
        <Scheduling
          groupSize={groupSize}
          timeSlot={timeSlot}
          onGroupSizeChange={handleGroupSizeChange} // Changed from props.onGroupSizeChange
          onTimeSlotChange={handleTimeSlotChange}
        />
        <Status isScheduled={props.isScheduled} />
        <Status isScheduled={!props.isScheduled} />
      </div>
    );
  }

  console.log(user);
  return (
    <>
      <Navigation /*isLoaded={isLoaded}*/ />
      <Routes>
        {user ? (
          //routes that will be available ONLY when user is logged in
          //add additional routes here
          <>
          <Route path="/" element={<RedirectToHome />} />
          <Route element={<Wrapper />} path="/home" />
          <Route element={       
          <Profile
          name={props.name}
          email={props.email}
          location={props.location}
          department={props.department}
          groupSize={groupSize}
          timeSlot={timeSlot}
          interests={props.interests}
          onGroupSizeChange={handleGroupSizeChange} // Changed from props.onGroupSizeChange
          onTimeSlotChange={handleTimeSlotChange} // Changed from props.onTimeSlotChange
        />
        } path="/profile" />
          </>
        ) : (
          // <Route element={<Profile />} path="/home" />
          //will redirect to '/' from any url if no user is logged in
          //do not add additional routes here
          <>
            <Route path="*" element={<Navigate to="/login" replace />} />
            <Route element={<Login />} path="/login" />
          </>
        )}
      </Routes>
    </>
  );
}

export default App;
