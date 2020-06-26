import React, { Component } from "react";
import axios from "axios";
import PropertyItem from "./PropertyItem";
import { Link } from "react-router-dom";

export class Property extends Component {
  state = {
    properties: [
      {name: "Apt 1"},
      {name: "Apt 2"}
    ],
  };

  // componentWillMount() {
  //   this.getProperties();
  // }

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
          className="jumbotron mt-3"
          style={{
            padding: "30px",
            boxShadow: "0 4px 8px 0 rgba(0,0,0,0.2)",
            borderRadius: "5px",
          }}
        >
          <h1 className="text-center" style={{ marginBottom: "20px" }}>
            Property List
          </h1>
          <ul className="list-group">{propertyItems}</ul>
          <div className="btn btn-primary mt-4" style={{ borderRadius: "4px" }}>
            <Link style={propertyLink} to="/property/add">
              Add Property
            </Link>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

const propertyLink = {
  color: "white",
  textDecoration: "none",
};

export default Property;
