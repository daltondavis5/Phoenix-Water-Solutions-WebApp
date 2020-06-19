import React, { Component } from "react";
import axios from "axios";
import ProviderItem from "./ProviderItem";

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
      <div className="jumbotron mt-3">
        <h1>Provider List</h1>
        <ul className="list-group">{providerItems}</ul>
      </div>
    );
  }
}

export default Provider;
