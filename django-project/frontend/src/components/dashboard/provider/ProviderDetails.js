import React, { Component } from "react";
import axios from "axios";
import UtilityProviderItem from "./UtilityProviderItem";
import UtilityProviderCard from "./UtilityProviderCard";

export class ProviderDetails extends Component {
  state = {
    name: "",
    utility_provider: [],
  };

  componentDidMount() {
    axios
      .get(`/api/provider/${this.props.match.params.id}`)
      .then((response) => {
        console.log(response.data)
        var alteredData = response.data.utility_provider.map((data) => {
          data.mode = "viewing";
          return data;
        });
        this.setState({
          name: response.data.name,
          utility_provider: alteredData,
        });
      });
    this.setState((prevState) => {
      prevState.utility_provider.map(
        (utility_provider_item) => (utility_provider_item["mode"] = "viewing")
      );
    });
  }

  changeToEdit = (index) => () => {
    let utility_provider = [...this.state.utility_provider];
    utility_provider[index]["mode"] = "editing";
    this.setState({
      utility_provider,
    });
  };

  changeToView = (index) => () => {
    let utility_provider = this.state.utility_provider[index];
    const body = {
      provider_name: this.state.name,
      utility_type: utility_provider.utility_type,
      city: utility_provider.city,
      state: utility_provider.state,
      unit_measurement: utility_provider.unit_measurement,
    };
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };

    if (utility_provider.mode == "adding") {
      axios
        .post("/api/utility_provider/", JSON.stringify(body), config)
        .then((response) => {});
    }
    if (utility_provider.mode == "editing") {
      axios
        .put(`/api/utility_provider/${utility_provider['id']}/`, JSON.stringify(body), config)
        .then((response) => {});
    }
    let utility_providers = [...this.state.utility_provider];
    utility_providers[index]["mode"] = "viewing";
    this.setState({
      utility_provider: utility_providers,
      currentMode: "added",
    });
  };

  handleChange = (index) => (e) => {
    let utility_provider = [...this.state.utility_provider];
    utility_provider[index][e.target.name] = e.target.value;
    this.setState({
      utility_provider,
    });
  };

  addUtilityProvider = (e) => {
    e.preventDefault();
    let utility_provider = this.state.utility_provider.concat([
      {
        utility_type: "",
        city: "",
        state: "",
        unit_measurement: "",
        mode: "adding",
      },
    ]);
    this.setState({
      utility_provider,
      currentMode: "adding",
    });
  };

  render() {
    const providerName = this.state.name;
    return (
      <React.Fragment>
        <h2 className="text-center">{this.state.name}</h2>
        {this.state.utility_provider.map((utility_provider_item, index) => {
          return utility_provider_item.mode === "viewing" ? (
            <UtilityProviderCard
              key={index}
              providerName={providerName}
              utility_provider_item={utility_provider_item}
              editButton={this.changeToEdit(index)}
            />
          ) : (
            <UtilityProviderItem
              key={index}
              providerName={providerName}
              saveButton={this.changeToView(index)}
              onChange={this.handleChange(index)}
              utility_provider_item={utility_provider_item}
            />
          );
        })}
        {this.state.currentMode !== "adding" && (
          <div className="form-group" style={{ marginTop: "20px" }}>
            <button
              onClick={this.addUtilityProvider}
              className="btn btn-outline-secondary"
            >
              Add New Utility
            </button>
          </div>
        )}
      </React.Fragment>
    );
  }
}

export default ProviderDetails;
