import React, { Component } from "react";

class MeterView extends Component {
  render() {
    const { name, utility_type } = this.props.meter;
    return (
      <div>
        <div className="card" style={{ borderRadius: "10px" }}>
          <div className="card-body">
            <ul className="list-group list-group-flush">
              <li className="list-group-item">Name: {name}</li>
              <li className="list-group-item">Utility: {utility_type}</li>
            </ul>
          </div>
        </div>

        <div className="edit-save-buttons" style={{ height: "76px" }}>
          <button
            type="submit"
            className="btn btn-primary float-right"
            style={{
              marginBottom: "20px",
              marginTop: "20px",
              width: "100px",
              borderRadius: "4px",
            }}
            onClick={this.props.changeToEdit}
          >
            Edit Meter
          </button>
        </div>
      </div>
    );
  }
}

export default MeterView;
