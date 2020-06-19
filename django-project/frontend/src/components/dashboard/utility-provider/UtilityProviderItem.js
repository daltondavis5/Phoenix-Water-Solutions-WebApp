import React, { Component } from "react";
import axios from "axios";

export class UtilityProviderItem extends Component {
  
  render() {
    const {
      utility_type,
      city,
      state,
      unit_measurement,
    } = this.props.utility_provider_item;

    return (
      <>
        <div className="form-group">
          <label>Utility Type:</label>
          <select
            className="form-control"
            name="utility_type"
            onChange={this.props.onChange}
            value={utility_type}
          >
            <option value="Default">Choose a utility</option>
            {this.props.utilities.map((utility) => {
              return (
                <option key={utility["utility_type"]} value={utility["utility_type"]}>
                  {utility["utility_type"]}
                </option>
              );
            })}
          </select>
        </div>
        <div className="form-group">
          <label>City</label>
          <input
            type="text"
            className="form-control"
            name="city"
            onChange={this.props.onChange}
            value={city}
          />
        </div>
        <div className="form-group">
          <label>State</label>
          <input
            type="text"
            className="form-control"
            name="state"
            onChange={this.props.onChange}
            value={state}
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
      </>
    );
  }
}

export default UtilityProviderItem;
