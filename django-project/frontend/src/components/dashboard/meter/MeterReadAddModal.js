import React, { Component } from "react";

export default class MeterReadAddModal extends Component {
  state = {
    id: "",
    amount: "",
    meter: "",
    time: "",
    date: "",
  };

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  addRead = () => {
    const data = {
      amount: this.state.amount,
      meter: this.state.meter,
      time: this.state.time,
      date: this.state.date,
    };
    this.props.addRead(data);
  };

  render() {
    return (
      <div
        className="modal fade"
        id="meterReadAdd"
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
                  <label>Amount</label>
                  <input
                    type="text"
                    className="form-control"
                    name="amount"
                    onChange={this.onChange}
                    value={this.state.amount}
                  />
                </div>
                <div className="form-group">
                  <label>Date</label>
                  <input
                    type="type"
                    className="form-control"
                    name="date"
                    placeholder="mm-dd-yyyy"
                    onChange={this.onChange}
                    value={this.state.date}
                  />
                </div>
                <div className="form-group">
                  <label>Time</label>
                  <input
                    type="text"
                    className="form-control"
                    name="time"
                    placeholder="hh:mm:ss"
                    onChange={this.onChange}
                    value={this.state.time}
                  />
                </div>
              </form>
            </div>
            <div className="modal-footer">
              <button
                type="button"
                className="btn btn-secondary"
                data-dismiss="modal"
                onClick={this.handleClose}
              >
                Close
              </button>
              <button
                type="button"
                className="btn btn-primary"
                onClick={this.addRead}
              >
                Save changes
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
