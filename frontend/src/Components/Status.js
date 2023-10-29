// Status.js

import React from 'react';
import './../SCSS/Status.css';

function Status(props) {
  return (
    <div className="status-container">
      {props.isScheduled ? (
        <p className="scheduled">Lunch meeting is scheduled!</p>
      ) : (
        <p className="not-scheduled">Request for the Lunch meeting is pending.</p>
      )}
    </div>
  );
}

export default Status;
