import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import Login from './Components/Login'; 
import {useSelector} from 'react-redux';  // import useSelector from react-redux
import { Route, Navigate, Routes } from 'react-router-dom';  // import Route and Navigate from react-router-dom

function App() {
  let user;
  const userDetails = {
    name: "John Doe",
    email: "johndoe@example.com",
    location: "New York, USA",
    department: "Engineering",
    groupSize: 3,
    profilePicture: "./profile.png",
    timeSlot: "10:00 AM - 11:00 AM",
    interests: ["Coding", "Traveling", "Reading"]
  };

  const [groupSize, setGroupSize] = useState(userDetails.groupSize);
  const [timeSlot, setTimeSlot] = useState(userDetails.timeSlot);

  const handleGroupSizeChange = (size) => {
    setGroupSize(size);
  }

  const handleTimeSlotChange = (slot) => {
    setTimeSlot(slot);
  }

  return (
    <div className="App">
      <header className="App-header">
        <Login />
        <Profile 
          name={userDetails.name} 
          email={userDetails.email}
          location={userDetails.location}
          department={userDetails.department}
          groupSize={groupSize}
          timeSlot={timeSlot}
          profilePicture={userDetails.profilePicture}
          interests={userDetails.interests}
          onGroupSizeChange={handleGroupSizeChange}
          onTimeSlotChange={handleTimeSlotChange}
        />
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
