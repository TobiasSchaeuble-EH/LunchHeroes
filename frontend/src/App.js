import logo from './logo.svg';
import './App.css';
import Login from './Components/Login';  // import the Login component

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Login /> {/* Add the Login component here */}
      </header>
    </div>
  );
}

export default App;
