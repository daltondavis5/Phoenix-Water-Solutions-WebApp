import React, { Component } from "react";
import UtilityProviderItem from "./UtilityProviderItem";
import axios from "axios";

export class ProviderForm extends Component {
  state = {
    name: "",
    utility_provider: [
      {
        utility_type: "",
        city: "",
        state: "",
        unit_measurement: "",
      },
    ],
    utilities: [],
  };

  componentDidMount() {
    axios.get("/api/utility/").then((response) => {
      this.setState({ utilities: response.data });
      console.log(this.state);
    });
  }

  onSubmit = (e) => {
    e.preventDefault();
    let name = this.state.name;
    let utility_provider = this.state.utility_provider;
    const body = JSON.stringify({ name, utility_provider });
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios.post("/api/provider/", body, config).then((res) => {
      console.log(res.data);
    });
  };

  onProviderChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
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
      },
    ]);
    this.setState({
      utility_provider,
    });
  };

  deleteUtilityProvider = (index) => (e) => {
    e.preventDefault();
    let utility_provider = [
      ...this.state.utility_provider.slice(0, index),
      ...this.state.utility_provider.slice(index + 1),
    ];
    this.setState({
      utility_provider,
    });
  };

  render() {
    const { name, utility_provider } = this.state;

    return (
      <div className="col-md-6 m-auto">
        <div className="card card-body mt-5">
          <h2 className="text-center">Add Provider Form</h2>
          <form onSubmit={this.onSubmit}>
            <div className="form-group">
              <label>Provider Name</label>
              <input
                type="text"
                className="form-control"
                name="name"
                onChange={this.onProviderChange}
                value={name}
              />
            </div>
            {utility_provider.map((utility_provider_item, index) => (
              <div key={index} className="card card-body my-2">
                <UtilityProviderItem
                  utility_provider_item={utility_provider_item}
                  utilities={this.state.utilities}
                  onChange={this.handleChange(index)}
                />
                <button
                  onClick={this.deleteUtilityProvider(index)}
                  className="btn btn-outline-danger"
                >
                  Delete Utility
                </button>
              </div>
            ))}

            <div className="form-group">
              <button
                onClick={this.addUtilityProvider}
                className="btn btn-outline-secondary"
              >
                Add New Utility
              </button>
              <button type="submit" className="btn btn-primary float-right">
                Submit Provider
              </button>
            </div>
          </form>
        </div>
      </div>
    );
  }
}

export default ProviderForm;
