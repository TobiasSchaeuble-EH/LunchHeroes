import React, { useState } from 'react';
// import logo from './logo.svg';
import './App.css';
import Login from './Components/Login';
import Navigation from './Components/Navigation';
import Status from './Components/Status';

import Scheduling from './Components/Scheduling';
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
      <div>
        <Scheduling
          groupSize={groupSize}
          timeSlot={timeSlot}
          onGroupSizeChange={handleGroupSizeChange} // Changed from props.onGroupSizeChange
          onTimeSlotChange={handleTimeSlotChange}
        />
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
        <Route element={
          <Wrapper
          />
        } path="/" />
         {user ? (
          //routes that will be available ONLY when user is logged in
          //add additional routes here
          <Route element={<Profile />} path="/home" />
        ) : (
          //will redirect to '/' from any url if no user is logged in
          //do not add additional routes here
          <Route path="*" element={<Navigate to="/" replace />} />
        )}
        <Route element={<Login />} path="/" /> 
      </Routes>
    </>
  );
}

export default App;
