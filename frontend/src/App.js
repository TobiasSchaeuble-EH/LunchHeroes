import logo from './logo.svg';
import './App.css';
import Login from './Components/Login';  // import the Login component

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <Routes>
        {user ? (
          //routes that will be available ONLY when user is logged in
          //add additional routes here
          <Route element={<Home />} path="/home" />
        ) : (
          //will redirect to '/' from any url if no user is logged in
          //do not add additional routes here
          <Route path="*" element={<Navigate to="/" replace />} />
        )}
        //login form will always be available //any route added here will always
        be available
        <Route element={<Login />} path="/" />
      </Routes>
      </header>
    </div>
  );
}

export default App;
