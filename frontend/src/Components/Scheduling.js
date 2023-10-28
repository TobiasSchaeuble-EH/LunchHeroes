import React from "react";
import "../SCSS/scheduling.css";

const Scheduling = (props) => {
  const generateTimeSlots = () => {
    let slots = [];
    for (let i = 0; i < 24; i++) {
      for (let j = 0; j < 60; j += 30) {
        const hour = String(i).padStart(2, "12:00");
        const minute = String(j).padStart(2, "0");
        slots.push(`${hour}:${minute}`);
      }
    }
    return slots;
  };

  const featureSoon = () => {
    window.alert("Feature coming soon!");
  }

  return (
    <div className="scheduling-container">
      <div className="scheduling-header">
        Fancy having lunch together with interesting people?
      </div>
      <div className="time-dropdown-guests-slider">
        <div className="time-dropdown">
          <div>
            <strong className="time-slot">Time Slot:</strong>
            <select
              value={props.timeSlot}
              onChange={(e) => props.onTimeSlotChange(e.target.value)}
            >
              {generateTimeSlots().map((slot, index) => (
                <option key={index} value={slot}>
                  {slot}
                </option>
              ))}
            </select>
          </div>
        </div>
        <div className="guests-slider">
          <div className="slider">
            <strong className="group-size">Group Size:</strong>
            <input
              type="range"
              min="2"
              max="4"
              value={props.groupSize}
              onChange={(e) => props.onGroupSizeChange(e.target.value)}
            />
            {props.groupSize} Persons
          </div>
        </div>
      </div>
      <div className="button-div">
        <button className="randomize-button">Randomize</button>
        <button className="customize-button" onClick={featureSoon}>Customize</button>
        <button className="view-all-button" onClick={featureSoon}>View All Settings</button>
      </div>
    </div>
  );
};

export default Scheduling;
