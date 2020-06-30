import React, { Component } from "react";
import { connect } from "react-redux";
import axios from "axios";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";

export class PropertyUnitItem extends Component {
  static propTypes = {
    createMessage: PropTypes.func.isRequired,
    returnErrors: PropTypes.func.isRequired,
  };

  state = {
    id: 0,
    name: "",
    propertyId: 0,
    editing: false,
    active: true,
  };

  switchToEdit = () => {
    this.setState({
      id: this.props.unit.id,
      name: this.props.unit.name,
      propertyId: this.props.unit.property,
      editing: true,
    });
  };

  updateUnit = () => {
    const body = {
      name: this.state.name,
      property: this.state.propertyId,
    };
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .put(`/api/unit/${this.state.id}/`, JSON.stringify(body), config)
      .then((response) => {
        this.props.createMessage({ msg: "Unit name updated!" });
        this.setState({
          editing: false,
        });
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
    this.setState({ editing: false });
  };

  deleteUnit = () => {
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios.delete(`/api/unit/${this.state.id}/`, config).then((response) => {
      this.props.createMessage({ msg: "Unit deleted!" });
      this.setState({
        active: false,
      });
    });
  };

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  render() {
    return (
      <>
        {this.state.active ? (
          this.state.editing ? (
            <div className="list-group-item">
              <h2 className="text-center">Edit Unit</h2>
              <form>
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
                    type="button"
                    className="btn btn-outline-primary float-right mx-2"
                    onClick={this.updateUnit}
                  >
                    Update
                  </button>
                  <button
                    type="button"
                    className="btn btn-outline-danger float-right"
                    onClick={this.deleteUnit}
                  >
                    Delete
                  </button>
                </div>
              </form>
            </div>
          ) : (
            <div className="list-group-item">
              {this.state.name !== "" ? this.state.name : this.props.unit.name}
              <button
                onClick={this.switchToEdit}
                className="btn btn-info float-right"
              >
                Edit
              </button>
            </div>
          )
        ) : (
          <></>
        )}
      </>
    );
  }
}

export default connect(null, { createMessage, returnErrors })(PropertyUnitItem);
