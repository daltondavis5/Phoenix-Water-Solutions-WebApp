import React, { Component } from "react";
import { connect } from "react-redux";
import axios from "axios";
import UtilityProviderItem from "./UtilityProviderItem";
import UtilityProviderCard from "./UtilityProviderCard";
import EditProvider from "./EditProvider";
import ViewProvider from "./ViewProvider";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";

export class ProviderDetails extends Component {
  state = {
    name: "",
    utility_provider: [],
    currentMode: "added",
    editingProviderName: false,
  };

  static propTypes = {
    createMessage: PropTypes.func.isRequired,
    returnErrors: PropTypes.func.isRequired,
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
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
    // TODO: Is setting the state again necessary??
    this.setState((prevState) => {
      prevState.utility_provider.map(
        (utility_provider_item) => (utility_provider_item["mode"] = "viewing")
      );
    });
  }

  updateName = (name) => {
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    const body = {
      name,
    };
    axios
      .put(
        `/api/provider/${this.props.match.params.id}/`,
        JSON.stringify(body),
        config
      )
      .then((response) => {
        this.setState({
          editingProviderName: false,
          name,
        });
        this.props.createMessage({
          msg: "Provider name successfully updated!",
        });
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  };

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
        .post("/api/utilityprovider/", JSON.stringify(body), config)
        .then((response) => {
          utility_provider["id"] = response.data.id;
          this.props.createMessage({ msg: "Success!" });
        })
        .catch((err) => {
          this.props.returnErrors(err.response.data, err.response.status);
        });
    }
    if (utility_provider.mode == "editing") {
      axios
        .put(
          `/api/utilityprovider/${utility_provider["id"]}/`,
          JSON.stringify(body),
          config
        )
        .then((response) => {
          this.props.createMessage({ msg: "Success!" });
        })
        .catch((err) => {
          this.props.returnErrors(err.response.data, err.response.status);
        });
    }
    let utility_providers = [...this.state.utility_provider];
    utility_providers[index]["mode"] = "viewing";
    this.setState({
      utility_provider: utility_providers,
      currentMode: "added",
    });
  };

  deleteItem = (index) => () => {
    let utility_provider = this.state.utility_provider[index];
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    if (utility_provider.mode == "editing") {
      axios
        .delete(`/api/utilityprovider/${utility_provider["id"]}/`, config)
        .then((response) => {});
    }
    let utility_providers = [
      ...this.state.utility_provider.slice(0, index),
      ...this.state.utility_provider.slice(index + 1),
    ];
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

  changeMode = () => {
    let currMode = this.state.editingProviderName;
    this.setState({
      editingProviderName: !currMode,
    });
  };

  render() {
    const providerName = this.state.name;
    return (
      <React.Fragment>
        <div className="mt-3">
          {this.state.editingProviderName ? (
            <EditProvider name={providerName} updateName={this.updateName} />
          ) : (
            <ViewProvider name={providerName} changeMode={this.changeMode} />
          )}
        </div>
        {this.state.utility_provider.map((utility_provider_item, index) => {
          return utility_provider_item.mode === "viewing" ? (
            <UtilityProviderCard
              key={index}
              providerName={providerName}
              utility_provider_item={utility_provider_item}
              editButton={this.changeToEdit(index)}
            />
          ) : (
            // editing or adding
            <UtilityProviderItem
              key={index}
              providerName={providerName}
              saveButton={this.changeToView(index)}
              deleteButton={this.deleteItem(index)}
              onChange={this.handleChange(index)}
              utility_provider_item={utility_provider_item}
            />
          );
        })}
        {this.state.currentMode !== "adding" && (
          <div className="form-group mt-4">
            <button
              onClick={this.addUtilityProvider}
              className="btn btn-outline-secondary rounded"
            >
              Add New Utility
            </button>
          </div>
        )}
      </React.Fragment>
    );
  }
}

export default connect(null, { createMessage, returnErrors })(ProviderDetails);
