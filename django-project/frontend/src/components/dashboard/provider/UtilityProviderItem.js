import React, { Component } from "react";
import axios from "axios";

export class UtilityProviderItem extends Component {
  state = {
    utilities: [],
    utility_type: "",
    state: "",
    city: "",
    unit_measurement: "",
  };

  componentDidMount() {
    axios.get("/api/utility/").then((response) => {
      this.setState({ utilities: response.data });
    });
    if (this.props.mode == "editing") {
      const { city, state, unit_measurement, utility_type } = this.props;
      this.setState({
        city,
        state,
        unit_measurement,
        utility_type,
      });
    }
  }

  saveData = () => {
    const METHOD = this.props.mode == "adding" ? "post" : "put";
    data = {
      city: this.state.city,
      state: this.state.state,
      unit_measurement: this.state.unit_measurement,
      utility_type: this.state.utility_type,
    };

    this.props.saveButton(data);
  };

  handleChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  render() {
    const mode = this.props.mode;
    return (
      <div style={{ marginBottom: "20px" }}>
        <h2 className="text-center">
          {mode === "adding" ? "Add a utility" : "Edit a utility"}
        </h2>
        <div className="edit-save-buttons" style={{ height: "25px" }}>
          <button
            type="submit"
            className="btn btn-primary float-right"
            style={{ marginLeft: "10px", width: "60px" }}
            onClick={this.saveData}
          >
            Save
          </button>
        </div>
        <div>
          <div className="form-group">
            <label>Utility Type</label>
            <select
              className="form-control"
              name="utility_type"
              onChange={this.handleChange}
              value={this.state.utility_type}
              disabled={mode == "editing"}
            >
              <option value="Default">Choose a utility</option>
              {this.state.utilities.map((utility) => {
                return (
                  <option
                    key={utility["utility_type"]}
                    value={utility["utility_type"]}
                  >
                    {utility["utility_type"]}
                  </option>
                );
              })}
            </select>
          </div>
          <div className="form-group">
            <label>State</label>
            <input
              type="text"
              className="form-control"
              name="state"
              onChange={this.handleChange}
              value={this.state.state}
              disabled={mode == "editing"}
            />
          </div>
          <div className="form-group">
            <label>City</label>
            <input
              type="text"
              className="form-control"
              name="city"
              onChange={this.handleChange}
              value={this.state.city}
              disabled={mode == "editing"}
            />
          </div>
          <div className="form-group">
            <label>Unit Measurement</label>
            <input
              type="text"
              className="form-control"
              name="unit_measurement"
              onChange={this.handleChange}
              value={this.state.unit_measurement}
            />
          </div>
        </div>
      </div>
    );
  }
}

export default UtilityProviderItem;
