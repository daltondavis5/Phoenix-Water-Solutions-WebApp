import React, { Component } from "react";

export default class MeterErrorEditModal extends Component {
  state = {
    id: "",
    description: "",
    meter: "",
    error_date: "",
    repair_date: "",
  };

  componentWillReceiveProps(props) {
    this.setState({
      id: props.id,
      description: props.description,
      meter: props.meter,
      error_date: props.error_date,
      repair_date: props.repair_date,
    });
  }

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  render() {
    return (
      <div
        className="modal fade"
        id="meterErrorEdit"
        tabIndex="-1"
        role="dialog"
        aria-labelledby="exampleModalCenterTitle"
        aria-hidden="true"
      >
        <div className="modal-dialog modal-dialog-centered" role="document">
          <div className="modal-content">
            <div className="modal-header">
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
              <form>
                <div className="form-group">
                  <label>Description</label>
                  <input
                    type="text"
                    className="form-control"
                    name="description"
                    onChange={this.onChange}
                    value={this.state.description}
                  />
                </div>
                <div className="form-group">
                  <label>Error Date</label>
                  <input
                    type="type"
                    className="form-control"
                    name="error_date"
                    placeholder="mm-dd-yyyy"
                    onChange={this.onChange}
                    value={this.state.error_date}
                  />
                </div>
                <div className="form-group">
                  <label>Repair Date</label>
                  <input
                    type="text"
                    className="form-control"
                    name="repair_date"
                    onChange={this.onChange}
                    value={
                      this.state.repair_date !== null
                        ? this.state.repair_date
                        : ""
                    }
                  />
                </div>
              </form>
            </div>
            <div className="modal-footer">
              <button
                type="button"
                className="btn btn-danger"
                data-dismiss="modal"
                onClick={this.deleteError}
              >
                Delete
              </button>
              <button
                type="button"
                className="btn btn-secondary"
                data-dismiss="modal"
                onClick={this.handleClose}
              >
                Close
              </button>
              <button type="button" className="btn btn-primary">
                Save changes
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
