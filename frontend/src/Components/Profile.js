import React from 'react';
import './../SCSS/Profile.css';

function Profile(props) {
    // Helper function to generate time slots
    const generateTimeSlots = () => {
        let slots = [];
        for (let i = 0; i < 24; i++) {
            for (let j = 0; j < 60; j += 30) {
                const hour = String(i).padStart(2, '0');
                const minute = String(j).padStart(2, '0');
                slots.push(`${hour}:${minute}`);
            }
        }
        return slots;
    };

    return (
      <div className="profile-container">
        {/* <img src={props.profilePicture} alt="Profile" className="profile-picture"/> */}
        <h2>{props.name}</h2>
        <div className="profile-detail">
          <strong>Email:</strong> {props.email}
        </div>
        <div className="profile-detail">
          <strong>Location:</strong> {props.location}
        </div>
        <div className="profile-detail">
          <strong>Department:</strong> {props.department}
        </div>
        <div className="profile-detail">
          <strong>Group Size:</strong>
          <input 
            type="range" 
            min="2" 
            max="4" 
            value={props.groupSize} 
            onChange={e => props.onGroupSizeChange(e.target.value)}
          />
          {props.groupSize} Persons
        </div>
        <div className="profile-detail">
          <strong>Time Slot:</strong>
          <select value={props.timeSlot} onChange={e => props.onTimeSlotChange(e.target.value)}>
            {generateTimeSlots().map((slot, index) => (
                <option key={index} value={slot}>{slot}</option>
            ))}
          </select>
        </div>
        <div className="profile-interests">
          <strong>Interests:</strong>
          <ul>
            {props.interests && props.interests.map((interest, index) => (
              <li key={index}>{interest}</li>
            ))}
          </ul>
        </div>
      </div>
    );
}

export default Profile;
