import './App.css'
import Header from "./components/Header.jsx";
import UserList from "./components/Users.jsx";

function App() {
  return (
    <>
      <Header />
      <div className="users-list">
        <UserList />
      </div>
    </>
  )
}

export default App
