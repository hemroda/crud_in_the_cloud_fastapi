import './App.css'
import UserList from "./components/Users.jsx";

function App() {
  return (
    <>
      <header>
        <h1 className="text-3xl font-bold">Crud@Cloud</h1>
      </header>
      <div className="users-list">
        <UserList />
      </div>
    </>
  )
}

export default App
