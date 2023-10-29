import React from 'react';
import './../SCSS/Status.css';

function Status(props) {
  return (
    <div className="status-container">
      {props.isScheduled ? (
        <>
          <p className="scheduled">Lunch meeting was successfully scheduled!</p>
          <div className="details">
            <p className="detail-item">Time <strong>{props.timeSlot}</strong></p>
            <p className="detail-item">Table Number <strong>{Math.floor(Math.random() * 4) + 1}</strong></p>
            <p className="detail-item">Guests: <strong>{Math.floor(Math.random() * 4) + 2}</strong></p>
          </div>
        </>
      ) : (
        <>
          <p className="not-scheduled">Request for the Lunch meeting is pending...</p>
          <div className="loading-bar-container">
            <div className="loading-bar-fill"></div>
          </div>
        </>
      )}
    </div>
  );
}

export default Status;
