import React, { Component } from "react";
import MeterSummaryItem from "./MeterSummaryItem";

export class MeterDashboard extends Component {
  state = {
    name: "",
    installed_date: "",
    uninstalled_date: null,
    utility: "",
  };

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  };

  addMeter = () => {
    let body = {
      name: this.state.name,
      utility: this.state.utility,
      installed_date: this.state.installed_date,
      uninstalled_date: this.state.uninstalled_date,
    };
    this.props.addMeter(body);
  };
  render() {
    const { name, installed_date, uninstalled_date, utility } = this.state;
    return (
      <>
        <div className="row row-cols-2">
          {this.props.meters.map((meter, i) => (
            <div className="col pb-3" key={i}>
              <MeterSummaryItem meter={meter} />
            </div>
          ))}
        </div>
        <span
          className="text-primary display-4"
          style={{
            position: "fixed",
            bottom: "20px",
            right: "20px",
            cursor: "pointer",
          }}
        >
          <i
            data-toggle="modal"
            data-target="#meterModal"
            className="fa fa-plus-circle"
          ></i>
        </span>

        <div
          className="modal fade"
          id="meterModal"
          tabIndex="-1"
          role="dialog"
          aria-labelledby="modalLabel"
          aria-hidden="true"
        >
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title" id="modalLabel">
                  Add New Meter
                </h5>
                <button
                  type="button"
                  className="close"
                  data-dismiss="modal"
                  aria-label="Close"
                >
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div className="modal-body">
                <div>
                  <div className="form-group">
                    <label>Name</label>
                    <input
                      type="text"
                      className="form-control"
                      name="name"
                      onChange={this.handleChange}
                      value={name}
                    />
                  </div>
                  <div className="form-group">
                    <label>Utility Type</label>
                    <select
                      className="form-control"
                      name="utility"
                      onChange={this.handleChange}
                      value={utility}
                    >
                      <option value="Default">Choose a utility</option>
                      {this.props.utilities.map((utility) => {
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
                      onChange={this.handleChange}
                      value={installed_date}
                    />
                  </div>
                  <div className="form-group">
                    <label>
                      Uninstalled Date{" "}
                      <span className="text-muted">(Optional)</span>
                    </label>
                    <input
                      type="date"
                      className="form-control"
                      name="uninstalled_date"
                      onChange={this.handleChange}
                      value={uninstalled_date !== null && uninstalled_date}
                    />
                  </div>
                </div>
              </div>
              <div className="modal-footer">
                <button
                  type="button"
                  className="btn btn-secondary"
                  data-dismiss="modal"
                >
                  Close
                </button>
                <button
                  type="button"
                  onClick={this.addMeter}
                  className="btn btn-primary"
                  data-dismiss="modal"
                >
                  Save
                </button>
              </div>
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default MeterDashboard;
