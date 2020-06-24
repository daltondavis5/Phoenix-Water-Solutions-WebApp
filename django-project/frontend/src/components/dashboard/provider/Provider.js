import React, { Component } from "react";
import axios from "axios";
import ProviderItem from "./ProviderItem";
import { Link } from "react-router-dom";

export class Provider extends Component {
  state = {
    providers: [],
  };

  componentWillMount() {
    this.getProviders();
  }

  getProviders = () => {
    axios
      .get("/api/provider")
      .then((response) => {
        this.setState({ providers: response.data });
      })
      .catch((err) => console.log(err));
  };
  render() {
    const providerItems = this.state.providers.map((provider, i) => (
      <ProviderItem key={i} provider={provider}></ProviderItem>
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
            Provider List
          </h1>
          <ul className="list-group">{providerItems}</ul>
          <div className="btn btn-primary mt-4" style={{ borderRadius: "4px" }}>
            <Link style={providerLink} to="/provider/add">
              Add Provider
            </Link>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

const providerLink = {
  color: "white",
  textDecoration: "none",
};

export default Provider;
