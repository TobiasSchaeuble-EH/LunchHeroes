import React, { useState } from 'react';
// import logo from './logo.svg';
import './App.css';
import Login from './Components/Login';
import Navigation from './Components/Navigation';
// import { useNavigate, useDispatch } from "react-router-dom";
import Profile from './Components/Profile';
import Status from './Components/Status';
import {useSelector} from 'react-redux';  // import useSelector from react-redux
import { Route, Navigate, Routes } from 'react-router-dom';  // import Route and Navigate from react-router-dom
import Scheduling from './Components/Scheduling';
import{ supabase } from './supabaseclient';



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
          onTimeSlotChange={handleTimeSlotChange}   // Changed from props.onTimeSlotChange
        />
        <Status isScheduled={props.isScheduled} />
        <Status isScheduled={!props.isScheduled} />
      </div>
    );
  }

  console.log(user);
  return (
    <>

    {/* <button onClick={async () => {
const {data} = await supabase.from('users').select('*, companies(*)')

console.log(data)

    }}>Test</button> */}
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
