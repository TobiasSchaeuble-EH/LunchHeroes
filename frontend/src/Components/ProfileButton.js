import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";

import { logout } from "../store/session";
import { useNavigate } from "react-router-dom";
import "../SCSS/navigation.css";
function ProfileButton({ user }) {
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();
  const navigate= useNavigate();
  const dispatch = useDispatch();
  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };
  useEffect(() => {
    if (!showMenu) return;
    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };
    document.addEventListener("click", closeMenu);
    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);
  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout())
    .then(() => {
      navigate("/");
      closeMenu();
    })
  };
  const navUserProfile = (e) => {
    e.preventDefault();
    navigate('/profile')
  }
  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);
  return (
    <>
      <button onClick={openMenu} className="user-profile-dropdown-button">
        {/* {user.username} */}
        <img
          className="profile-button-picture"
          src="icons/profile-button.png"
          alt="profile button"
        />
      </button>
      <ul className={ulClassName} ref={ulRef}>
          <>
            <div className="user-dropdown-menu">
              <button className="drop-down-profile-settings" onClick={navUserProfile}>Profile Settings</button>
              <button onClick={handleLogout} className="drop-down-sign-out">
                Sign Out
              </button>
            </div>
          </>
      </ul>
    </>
  );
}
export default ProfileButton;
