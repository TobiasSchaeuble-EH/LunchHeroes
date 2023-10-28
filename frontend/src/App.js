import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import Login from './Components/Login'; 
import Profile from './Components/Profile'; 

function App() {
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
      </header>
    </div>
  );
}

export default App;
