import React, { Component } from "react";
import axios from "axios";

export class UtilityProviderItem extends Component {
  state = {
    utilities: [],
  };

  componentDidMount() {
    axios.get("/api/utility/").then((response) => {
      this.setState({ utilities: response.data });
    });
  }

  render() {
    const {
      utility_type,
      city,
      state,
      unit_measurement,
      mode,
    } = this.props.utility_provider_item;
    return (
      <div style={{ marginBottom: "20px" }}>
        <h2 className="text-center">
          {mode === "adding" ? "Add a utility" : "Edit a utility"}
        </h2>
        <div className="edit-save-buttons" style={{ height: "25px" }}>
          <button
            type="submit"
            className="btn btn-primary float-right"
            style={{ marginLeft: "10px", width: "60px", borderRadius: "4px" }}
            onClick={this.props.saveButton}
          >
            Save
          </button>
          <button
            type="submit"
            className="btn btn-danger float-right"
            style={{ marginLeft: "10px", width: "70px", borderRadius: "4px" }}
            onClick={this.props.deleteButton}
          >
            Delete
          </button>
        </div>
        <div>
          <div className="form-group">
            <label>Utility Type</label>
            <select
              className="form-control"
              name="utility_type"
              onChange={this.props.onChange}
              value={utility_type}
              disabled={mode == "editing"}
            >
              <option value="Default">Choose a utility</option>
              {this.state.utilities.map((utility) => {
                return (
                  <option key={utility["type"]} value={utility["type"]}>
                    {utility["type"]}
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
              onChange={this.props.onChange}
              value={state}
              disabled={mode == "editing"}
            />
          </div>
          <div className="form-group">
            <label>City</label>
            <input
              type="text"
              className="form-control"
              name="city"
              onChange={this.props.onChange}
              value={city}
              disabled={mode == "editing"}
            />
          </div>
          <div className="form-group">
            <label>Unit Measurement</label>
            <input
              type="text"
              className="form-control"
              name="unit_measurement"
              onChange={this.props.onChange}
              value={unit_measurement}
            />
          </div>
        </div>
      </div>
    );
  }
}

export default UtilityProviderItem;
