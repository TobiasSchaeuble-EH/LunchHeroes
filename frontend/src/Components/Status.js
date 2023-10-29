import React from 'react';
import './../SCSS/Status.css';

function Status(props) {
  return (
    <div className="status-container">
      {props.isScheduled ? (
        <>
          <p className="scheduled">Lunch meeting was successfully scheduled!</p>
          <div className="details">
            <p className="detail-item">Time <strong>12:00</strong></p>
            <p className="detail-item">Table Number <strong>12</strong></p>
            <p className="detail-item">Guests: <strong>4</strong></p>
          </div>
        </>
      ) : (
        <p className="not-scheduled">Request for the Lunch meeting is pending...</p>
      )}
    </div>
  );
}

export default Status;
