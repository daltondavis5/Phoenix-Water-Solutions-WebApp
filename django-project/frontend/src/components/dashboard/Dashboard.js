import React, { Component } from "react";
import Provider from "./provider/Provider";
import Property from "./property/Property";

export class Dashboard extends Component {
  render() {
    return (
      <div>
        <Provider></Provider>
        <Property></Property>
      </div>
    );
  }
}

export default Dashboard;
