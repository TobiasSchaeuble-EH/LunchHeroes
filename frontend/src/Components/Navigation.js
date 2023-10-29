import React, { useState, useEffect, useRef } from "react";
import { Link } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import ProfileButton from "./ProfileButton";
import { logout } from "../store/session";
import "../SCSS/navigation.css";

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const dispatch = useDispatch();
  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
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
  const closeMenu = () => setShowMenu(false);
  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };
  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");

  return (

    <>
      <div className="nav-div-user-logged-in">
        <div className="nav-icon-user-logged-in">
          <Link exact to="/home">
            <img className="responsive-logo" alt="Here the Basel Hack Logo is displayed" src="/Logo.svg" />
            <img className="responsive-logo" alt="Here the Basel Hack Logo is displayed" src="/burger_wink.svg" />
          </Link>
        </div>
        <div className="profile-create-user-logged-in">
          <div className={ulClassName} ref={ulRef}></div>
          {/* {isLoaded && ( */}
          <div className="profile-button-user-logged-in">
            <ProfileButton user={sessionUser} />
          </div>
          {/* )} */}
        </div>
      </div>
      <span className="divider"></span>
    </>
  );
}

export default Navigation;
