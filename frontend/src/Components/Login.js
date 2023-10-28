import React, { useState } from 'react';
import {useDispatch} from 'react-redux';
import { login } from '../store/session';
import './../SCSS/Login.css';
import { useNavigate } from "react-router-dom";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState('');
  const dispatch = useDispatch();
  const nav = useNavigate();



  const handleSubmit = (e) => {
    e.preventDefault();
    // Here you can send the username and password to your server
    dispatch(login(email, password))
    .then(() => {
      nav("/home");
    })
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Email:
            <input
              type="text"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </label>
        </div>
        <div>
          <label>
            Password:
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </label>
        </div>
        <div>
          <button type="submit" onClick={handleSubmit}>
            Login
          </button>
        </div>
      </form>
    </div>
  );
}

export default Login;
