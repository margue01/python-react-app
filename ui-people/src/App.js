
import React from 'react';
import Users from "./Users";

const renderTitle = () => (
  <h1>Python and React App example</h1>
)

export default function App() {
    return (
      <div>
        { renderTitle() }
        <Users/>
      </div>
    )
}
