import React, { Component } from "react";
import { connect } from "react-redux";
import axios from "axios";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";
import PropertyUnitItem from "./PropertyUnitItem";

class PropertyUnits extends Component {
  static propTypes = {
    createMessage: PropTypes.func.isRequired,
    returnErrors: PropTypes.func.isRequired,
  };

  state = {
    adding: false,
    name: "",
  };

  addUnit = () => {
    this.setState({ adding: true });
  };

  onSubmit = (e) => {
    e.preventDefault();
    const body = {
      name: this.state.name,
      property: this.props.propertyId,
    };
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .post("/api/unit/", JSON.stringify(body), config)
      .then((res) => {
        this.props.createMessage({
          msg: `Successfully added Unit - ${this.state.name}`,
        });
        this.setState({
          adding: false,
        });
        window.location.reload();
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });

    // make a call to parent component to update the unit list - current fix is to reload the page
    //this.props.refreshUnitList();
  };

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  render() {
    const propertyUnitItems = this.props.units.map((unit, i) => (
      <PropertyUnitItem key={i} unit={unit}></PropertyUnitItem>
    ));
    return (
      <React.Fragment>
        <ul className="list-group">{propertyUnitItems}</ul>
        <button
          onClick={this.addUnit}
          className="btn btn-outline-primary mt-3 rounded"
        >
          Add New Unit
        </button>
        {this.state.adding ? (
          <div className="card card-body mt-3">
            <h2 className="text-center">Add Unit</h2>
            <form onSubmit={this.onSubmit}>
              <div className="form-group">
                <label>Unit Name</label>
                <input
                  type="text"
                  className="form-control"
                  name="name"
                  onChange={this.onChange}
                  value={this.state.name}
                />
              </div>
              <div className="form-group">
                <button
                  type="submit"
                  className="btn btn-outline-primary float-right"
                >
                  Save Unit
                </button>
              </div>
            </form>
          </div>
        ) : null}
      </React.Fragment>
    );
  }
}

export default connect(null, { createMessage, returnErrors })(PropertyUnits);
