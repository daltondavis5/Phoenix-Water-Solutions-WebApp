import React, { Component } from "react";

class MeterPropertiesView extends Component {
  render() {
    const {
      name,
      utility,
      installed_date,
      uninstalled_date,
    } = this.props.meter;
    return (
      <div>
        <div className="card mt-5 mb-5 shadow" style={{ borderRadius: "10px" }}>
          <div className="card-body">
            <div className="edit-save-buttons" style={{ height: "25px" }}>
              <button
                type="submit"
                className="btn btn-primary float-right rounded"
                onClick={this.props.changeToEdit}
              >
                Edit Meter
              </button>
            </div>
            <ul className="list-group list-group-flush mt-3">
              <li className="list-group-item">Name: {name}</li>
              <li className="list-group-item">Utility: {utility}</li>
              <li className="list-group-item">
                Installed Date: {installed_date}
              </li>
              <li className="list-group-item">
                Uninstalled Date: {uninstalled_date}
              </li>
            </ul>
          </div>
        </div>
      </div>
    );
  }
}

export default MeterPropertiesView;
