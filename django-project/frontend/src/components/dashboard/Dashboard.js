import React, { Component } from "react";

export class Dashboard extends Component {
  state = {
    providername: "",
    utilityname: "",
    city: "",
    state: "",
    unitmeasurement: "",
  };

  onSubmit = (e) => {
    e.preventDefault();
  };

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  render() {
    const {
      providername,
      utilityname,
      city,
      state,
      unitmeasurement,
    } = this.state;

    return (
      <div className="col-md-6 m-auto">
        <div className="card card-body mt-5">
          <h2 className="text-center">Add Provider Form</h2>
          <form onSubmit={this.onSubmit}>
            <div className="form-group">
              <label>Provider Name</label>
              <input
                type="text"
                className="form-control"
                name="providername"
                onChange={this.onChange}
                value={providername}
              />
            </div>
            <div className="form-group">
              <label>Utility Name</label>
              <input
                type="text"
                className="form-control"
                name="utilityname"
                onChange={this.onChange}
                value={utilityname}
              />
            </div>
            <div className="form-group">
              <label>City</label>
              <input
                type="text"
                className="form-control"
                name="city"
                onChange={this.onChange}
                value={city}
              />
            </div>
            <div className="form-group">
              <label>State</label>
              <input
                type="text"
                className="form-control"
                name="state"
                onChange={this.onChange}
                value={state}
              />
            </div>
            <div className="form-group">
              <label>Unit Measurement</label>
              <input
                type="text"
                className="form-control"
                name="unitmeasurement"
                onChange={this.onChange}
                value={unitmeasurement}
              />
            </div>
            <div className="form-group">
              <button type="submit" className="btn btn-primary">
                Add Provider
              </button>
            </div>
          </form>
        </div>
      </div>
    );
  }
}

export default Dashboard;
