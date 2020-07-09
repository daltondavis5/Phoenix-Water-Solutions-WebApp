import React, { Component } from "react";
import axios from "axios";
import PropertyItem from "./PropertyItem";
import { Link } from "react-router-dom";

export class Property extends Component {
  state = {
    properties: [],
  };

  componentWillMount() {
    this.getProperties();
  }

  getProperties = () => {
    axios
      .get("/api/property")
      .then((response) => {
        this.setState({ properties: response.data });
      })
      .catch((err) => console.log(err));
  };
  render() {
    const propertyItems = this.state.properties.map((property, i) => (
      <PropertyItem key={i} property={property}></PropertyItem>
    ));

    return (
      <React.Fragment>
        <div
          className="jumbotron mt-3 rounded shadow"
          style={{
            padding: "30px",
            backgroundImage:
              "radial-gradient( circle 592px at 48.2% 50%,  rgba(255,255,249,0.6) 0%, rgba(160,199,254,1) 74.6% )",
          }}
        >
          <h1 className="text-center mb-4">Property List</h1>
          <ul className="list-group">{propertyItems}</ul>
          <div className="btn btn-primary mt-4 rounded d-flex justify-content-center">
            <Link
              className="text-white text-decoration-none"
              to="/property/add"
            >
              Add Property
            </Link>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default Property;
