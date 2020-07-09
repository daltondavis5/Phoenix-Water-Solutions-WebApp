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
              "radial-gradient( circle 592px at 48.2% 50%,  rgba(245,247,252,1) 0%, rgba(137,171,245,0.37) 75% )",
          }}
        >
          <h1 className="text-center mb-4">Property List</h1>
          <ul className="list-group">{propertyItems}</ul>
          <div className="btn btn-primary mt-4 rounded w-25 mx-auto d-flex justify-content-center">
            <Link
              className="text-light text-decoration-none"
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
