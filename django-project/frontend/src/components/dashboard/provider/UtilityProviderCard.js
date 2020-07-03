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
            className="btn btn-primary float-right rounded"
            style={{ width: "60px" }}
            onClick={this.props.editButton}
          >
            Edit
          </button>
        </div>
        <div className="card" style={{ borderRadius: "10px" }}>
          <div className="card-body">
            <ul className="list-group list-group-flush">
              <li className="list-group-item">Utility: {utility_type}</li>
              <li className="list-group-item">State: {state}</li>
              <li className="list-group-item">City: {city}</li>
              <li className="list-group-item">
                Unit Measurement: {unit_measurement}
              </li>
            </ul>
          </div>
        </div>
      </div>
    );
  }
}

export default UtilityProviderCard;
