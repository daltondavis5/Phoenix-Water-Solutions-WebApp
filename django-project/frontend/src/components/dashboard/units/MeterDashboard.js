import React, { Component } from "react";
import MeterSummaryItem from "./MeterSummaryItem";

export class MeterDashboard extends Component {
  render() {
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
          }}
        >
          <i
            onClick={this.addMeter}
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
                body
                {/* <div>
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
                      onChange={this.props.onChange}
                      value={installed_date}
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
                </div> */}
              </div>
              <div className="modal-footer">
                <button
                  type="button"
                  className="btn btn-secondary"
                  data-dismiss="modal"
                >
                  Close
                </button>
                <button type="button" className="btn btn-primary">
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
