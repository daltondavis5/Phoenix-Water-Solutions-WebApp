import React, { Component } from "react";
import { connect } from "react-redux";
import { Link } from "react-router-dom";
import axios from "axios";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";

export class AddProperty extends Component {
  state = {
    name: "",
    address: "",
    zipcode: "",
    response: "",
  };

  static propTypes = {
    returnErrors: PropTypes.func.isRequired,
  };

  onSubmit = (e) => {
    const { name, address, zipcode } = this.state;
    const body = {
      name,
      street_address: address,
      zip_code: zipcode,
      attribute: false,
    };
    e.preventDefault();
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .post("/api/property/", JSON.stringify(body), config)
      .then((res) => {
        this.props.createMessage({
          msg: `Successfully added Property - ${name}`,
        });
        // redirectly directing to property details page
        this.props.history.push(`/property/${res.data.id}`);
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  };

  onChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  };

  render() {
    return (
      <React.Fragment>
        <div className="col-md-6 m-auto">
          <div className="card card-body mt-5">
            <h2 className="text-center">Add Property Form</h2>
            <form onSubmit={this.onSubmit}>
              <div className="form-group">
                <label>Property Name</label>
                <input
                  type="text"
                  className="form-control"
                  name="name"
                  required
                  onChange={this.onChange}
                  value={this.state.name}
                />
              </div>
              <div className="form-group">
                <label>Street address</label>
                <input
                  type="text"
                  className="form-control"
                  name="address"
                  required
                  onChange={this.onChange}
                  value={this.state.address}
                />
              </div>
              <div className="form-group">
                <label>Zipcode</label>
                <input
                  type="text"
                  className="form-control"
                  name="zipcode"
                  required
                  onChange={this.onChange}
                  value={this.state.zipcode}
                />
              </div>
              <button
                type="submit"
                className="btn btn-primary"
                style={{ borderRadius: "2px" }}
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

export default connect(null, { createMessage, returnErrors })(AddProperty);
