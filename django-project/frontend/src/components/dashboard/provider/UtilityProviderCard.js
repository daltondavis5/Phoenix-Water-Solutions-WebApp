import React, { Component } from "react";

class UtilityProviderCard extends Component {
  render() {
    const {
      city,
      state,
      unit_measurement,
      utility_type,
    } = this.props.utility_provider_item;
    return (
      <div style={{ marginBottom: "20px" }}>
        <div className="edit-save-buttons" style={{ height: "40px" }}>
          <button
            type="submit"
            className="btn btn-primary float-right"
            style={{ marginLeft: "10px", width: "60px", borderRadius: "4px" }}
            onClick={this.props.editButton}
          >
            Edit
          </button>
        </div>
        <div className="card" style={{borderRadius: "10px"}}>
          <div className="card-body">Utility: {utility_type}</div>
          <div className="card-body">State: {state}</div>
          <div className="card-body">City: {city}</div>
          <div className="card-body">Unit Measurement: {unit_measurement}</div>
        </div>
      </div>
    );
  }
}

export default UtilityProviderCard;
