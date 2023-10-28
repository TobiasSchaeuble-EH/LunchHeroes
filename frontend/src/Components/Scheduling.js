import React from "react";
import "../SCSS/scheduling.css";

const Scheduling = () => {
  return(
  <div className="scheduling-container">
    <div className="scheduling-header">
        Fancy having lunch together with interesting people?
    </div>
    <div className="time-dropdown-guests-slider">
        <div className="time-dropdown">
            <div className="time">Time: </div>
            <div>dropdown for time</div>
        </div>
        <div className="guests-slider">
            <div className="guests">Guests: </div>
            <div className="slider">slider for # of guests</div>
        </div>
    </div>
    <div className="button-div">
        <button className="randomize-button">Randomize</button>
        <button className="customize-button">Customize</button>
        <button className="view-all-button">View All</button>
    </div>
  </div>
  );
};

export default Scheduling;
