import React from "react";

const Header = () => {
  return (
    <header className="flex justify-between items-center w-full max-w-5xl">
      <h1 className="text-3xl font-bold">Crud@Cloud</h1>
      <nav>
        <ul>
          <li><a href="/api/users/">Users</a></li>
        </ul>
      </nav>
    </header>
  )
}

export default Header;
