import React from "react";
import "../SCSS/scheduling.css";

const Scheduling = (props) => {
  const generateTimeSlots = () => {
    let slots = [];
    for (let i = 11; i <= 14; i++) {
        for (let j = 0; j < 60; j += 30) {
            if (i === 14 && j > 0) break;  // Avoid adding 14:30
            const hour = String(i).padStart(2, '0');
            const minute = String(j).padStart(2, '0');
            slots.push(`${hour}:${minute}`);
        }
    }
    return slots;
};

  return (
<div className="scheduling-container">
  <div className="scheduling-header">
    Fancy having lunch together with interesting people?
  </div>
  <div className="time-dropdown-guests-slider">
        <div className="time-dropdown">
          <div>
            <strong>Time Slot:</strong>
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
            <strong>Group Size:</strong>
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
  <div className="actions-container">
    <div className="quick-actions">
      <button className="randomize-button">Randomize</button>
      <p>Use default settings for a quick match.</p>
    </div>
    <div className="advanced-actions">
      <button className="customize-button">Customize</button>
      <p>Adjust settings to find your perfect match.</p>
    </div>
  </div>
  <div className="view-all-container">
    <button className="view-all-button">View All Matches</button>
  </div>
</div>
  );
};

export default Scheduling;
