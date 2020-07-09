import React, { Component } from "react";
import Provider from "./provider/Provider";
import Property from "./property/Property";

export class Dashboard extends Component {
  render() {
    return (
      <div className="row w-75 m-auto">
        <div className="col-sm-12">
          <Provider></Provider>
        </div>
        <div className="col-sm-12">
          <Property></Property>
        </div>
      </div>
    );
  }
}

export default Dashboard;
