import React, { Component } from "react";
import ReactDOM from "react-dom";
import Dashboard from "./dashboard/Dashboard";

class App extends Component {
  render() {
    return (
      <>
        <Dashboard></Dashboard>
      </>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
