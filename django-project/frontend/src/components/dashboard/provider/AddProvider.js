import React, { Component } from "react";
import { connect } from "react-redux";
import axios from "axios";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";

export class AddProvider extends Component {
  state = {
    name: "",
    response: "",
  };

  static propTypes = {
    returnErrors: PropTypes.func.isRequired,
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
        this.props.createMessage({
          msg: `Successfully added Provider - ${name}`,
        });
        // redirectly directing to provider details page
        this.props.history.push(`/provider/${res.data.id}`);
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
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
              <button
                type="submit"
                className="btn btn-primary rounded"
              >
                Submit
              </button>
            </form>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default connect(null, { createMessage, returnErrors })(AddProvider);
