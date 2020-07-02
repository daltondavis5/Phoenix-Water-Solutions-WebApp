import React, { Component } from "react";
import axios from "axios";

class MeterEdit extends Component {
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
      name,
      utility_type,
      installed_date,
      uninstalled_date,
      mode,
    } = this.props.meter;
    return (
      <React.Fragment>
        <div className="card" style={{ marginBottom: "20px" }}>
          <div className="card-body">
            <h2 className="text-center">
              {mode === "adding" ? "Add Meter" : "Edit Meter"}
            </h2>
            <div className="edit-save-buttons" style={{ height: "25px" }}>
              <button
                type="submit"
                className="btn btn-primary float-right"
                style={{
                  marginLeft: "10px",
                  width: "60px",
                  borderRadius: "4px",
                }}
                onClick={this.props.saveButton}
              >
                Save
              </button>
              <button
                type="submit"
                className="btn btn-danger float-right"
                style={{
                  marginLeft: "10px",
                  width: "70px",
                  borderRadius: "4px",
                }}
                onClick={this.props.deleteButton}
              >
                Delete
              </button>
            </div>
            <div>
              <div className="form-group">
                <label>Name</label>
                <input
                  type="text"
                  className="form-control"
                  name="name"
                  onChange={this.props.onChange}
                  value={name}
                />
              </div>
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
                <label>Installed Date</label>
                <input
                  type="date"
                  className="form-control"
                  name="installed_date"
                  onChange={this.props.onChange}
                  value={installed_date}
                  disabled={mode == "editing"}
                />
              </div>
              <div className="form-group">
                <label>Uninstalled Date</label>
                <input
                  type="date"
                  className="form-control"
                  name="uninstalled_date"
                  onChange={this.props.onChange}
                  value={uninstalled_date !== null && uninstalled_date}
                />
              </div>
            </div>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default MeterEdit;
