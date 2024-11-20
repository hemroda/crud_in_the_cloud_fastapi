import React, { useEffect, useState} from "react";
import api from "../api.js";
import AddUserForm from "./AddUserForm.jsx";

const UserList = () => {
  const [users, setUsers] = useState([]);

  const fetchUsers = async () => {
    try {
      const response = await api.get("/api/users/")
      setUsers(response.data);
    } catch (error) {
      console.error("Error fetching users", error)
    }
  };

  const addUser = async (userEmail, userPassword) => {
    try {
      await api.post("/api/users/", { email: userEmail, password: userPassword });
      fetchUsers();
    } catch (error) {
      console.error("Error adding user", error)
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
      <div className="mt-10">
        <AddUserForm addUser={addUser} />
        <h2>Users List</h2>
        <ul>
          {users.map((user) => (
              <li key={user.id} className="card">{user.email}</li>
          ))}
        </ul>
      </div>
  )
};

export default UserList;
