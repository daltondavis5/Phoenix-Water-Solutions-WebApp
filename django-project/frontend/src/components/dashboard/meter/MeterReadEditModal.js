import React, { Component } from "react";

export default class MeterReadEditModal extends Component {
  state = {
    id: "",
    amount: "",
    meter: "",
    time: "",
    date: "",
    mode: "",
  };

  componentWillReceiveProps(props) {
    this.setState({
      id: props.id,
      amount: props.amount,
      meter: props.meter,
      time: props.isoDate.time,
      date: props.isoDate.date,
      mode: props.mode,
    });
  }
  

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  render() {
    return (
      <div
        className="modal fade"
        id="meterReadEdit"
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
