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
          className="jumbotron mt-3 rounded shadow"
          style={{
            padding: "30px",
            backgroundImage:
              "radial-gradient( circle 592px at 48.2% 50%,  rgba(245,247,252,1) 0%, rgba(137,171,245,0.37) 75% )",
          }}
        >
          <h1 className="text-center mb-4">Provider List</h1>
          <ul className="list-group">{providerItems}</ul>
          <div className="btn btn-primary mt-4 rounded w-25 mx-auto d-flex justify-content-center">
            <Link
              className="text-white text-decoration-none"
              to="/provider/add"
            >
              Add Provider
            </Link>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default Provider;
