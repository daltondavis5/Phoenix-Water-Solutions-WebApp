import React, { Component } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

export class AddProvider extends Component {
  state = {
    name: "",
    status: "adding",
    response: "",
    utility_provider: [],
  };

  onSubmit = (e) => {
    const { name } = this.state;
    e.preventDefault();
    const body = JSON.stringify({ name });
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .post("/api/provider/", body, config)
      .then((res) => {
        this.setState({
          response: res.data,
          status: "added",
        });
      })
      .catch((err) => {
        // this.props.returnErrors(err.response.data, err.response.status);
      });
  };

  onChange = (e) => {
    this.setState({
      name: e.target.value,
    });
  };

  render() {
    return (
      <React.Fragment>
        <div className="col-md-6 m-auto">
          <div className="card card-body mt-5">
            <h2 className="text-center">Add Provider Form</h2>
            <form onSubmit={this.onSubmit}>
              <div className="form-group">
                <label>Provider Name</label>
                <input
                  type="text"
                  className="form-control"
                  name="name"
                  onChange={this.onChange}
                  value={this.state.name}
                />
              </div>
              {this.state.status !== "added" && (
                <button type="submit" className="btn btn-primary">
                  Submit
                </button>
              )}
              {this.state.status === "added" && (
                <div className="btn btn-primary">
                  <Link
                    style={providerLink}
                    to={`/provider/${this.state.response["id"]}`}
                  >
                    Add Utility
                  </Link>
                </div>
              )}
            </form>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

const providerLink = {
  color: "white",
  textDecoration: "none",
};

export default AddProvider;
