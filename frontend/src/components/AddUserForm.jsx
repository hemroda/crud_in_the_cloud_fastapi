import React, {useState} from "react";

const AddUserForm = ({addUser}) => {
  const [userEmail, setUserEmail] = useState("");
  const [userPassword, setUserPassword] = useState("")

  const handleSubmit = (event) => {
    event.preventDefault();
    if (userEmail && userPassword) {
      addUser(userEmail, userPassword);
      setUserEmail((""));
      setUserPassword((""));
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col my-2 space-y-2">
      <input
        type="text"
        value={userEmail}
        onChange={(e) => setUserEmail(e.target.value)}
        placeholder="User email"
        className="form-field"
      />
      <input
        type="password"
        value={userPassword}
        onChange={(e) => setUserPassword((e.target.value))}
        placeholder="User password"
        className="form-field"
      />
      <button type="submit">Add User</button>
    </form>
  )
};

export default AddUserForm;
