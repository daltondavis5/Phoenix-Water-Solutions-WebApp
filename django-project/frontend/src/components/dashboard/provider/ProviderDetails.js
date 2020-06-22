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

  changeToEdit = (card) => {
    var changeMode = this.state.utility_provider.map((item) => {
      if (
        item.utility_type == card.utility_type &&
        item.state == card.state &&
        item.city == card.city
      ) {
        item.mode = "editing";
      }
      return item;
    });
    this.setState({
      utility_provider: changeMode,
    });
  };

  changeToView = (card) => {
    var changeMode = this.state.utility_provider.map((item) => {
      if (
        item.utility_type == card.utility_type &&
        item.state == card.state &&
        item.city == card.city
      ) {
        item.mode = "viewing";
      }
      return item;
    });
    this.setState({
      utility_provider: changeMode,
    });
  }

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
    return (
      <React.Fragment>
        <h2 className="text-center">{this.state.name}</h2>
        {this.state.utility_provider.map((utility_provider_item ,index) => {
          return utility_provider_item.mode === "viewing" ? (
            <UtilityProviderCard
              key={index}
              city={utility_provider_item.city}
              state={utility_provider_item.state}
              unit_measurement={utility_provider_item.unit_measurement}
              utility_type={utility_provider_item.utility_type}
              editButton={this.changeToEdit}
            />
          ) : (
            <UtilityProviderItem
              key={index}
              city={utility_provider_item.city}
              state={utility_provider_item.state}
              unit_measurement={utility_provider_item.unit_measurement}
              utility_type={utility_provider_item.utility_type}
              mode={utility_provider_item.mode}
              saveButton={this.changeToView}
            />
          );
        })}
        {this.state.currentMode !== "adding" && (
          <div className="form-group" style={{marginTop: '20px'}}>
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
