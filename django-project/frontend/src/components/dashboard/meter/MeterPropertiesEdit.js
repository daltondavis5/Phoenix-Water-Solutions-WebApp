import React, { Component } from "react";
import { connect } from "react-redux";
import axios from "axios";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";
import { Redirect } from "react-router-dom";

class MeterPropertiesEdit extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: props.meter.name,
      utility: props.meter.utility,
      installed_date: props.meter.installed_date,
      uninstalled_date: props.meter.uninstalled_date,
      id: props.meter.id,
      unit: props.meter.unit,
    };
  }

  static propTypes = {
    createMessage: PropTypes.func.isRequired,
    returnErrors: PropTypes.func.isRequired,
  };

  onChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  };

  saveButton = () => {
    const body = {
      name: this.state.name,
      utility: this.state.utility,
      installed_date: this.state.installed_date,
      uninstalled_date: this.state.uninstalled_date,
      id: this.state.id,
      unit: this.state.unit,
    };
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .put(`/api/meter/${this.state.id}/`, JSON.stringify(body), config)
      .then((response) => {
        this.props.createMessage({ msg: "Success!" });
        this.props.updateMeter(body);
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  };

  deleteMeter = () => {
    const { id, unit } = this.state;
    const body = {
      id,
    };
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .delete(`/api/meter/${id}/`, JSON.stringify(body), config)
      .then((res) => {
        this.props.createMessage({
          msg: `Successfully deleted`,
        });
        // redirectly directing to provider details page
        // this.props.history.push(`/unit/${unit}`);
        <Redirect to="/unit/:id" />;
      })
      .catch((err) => {
        // this.props.returnErrors(err.response.data, err.response.status);
      });
  };

  render() {
    const { name, utility, installed_date, uninstalled_date } = this.state;
    return (
      <React.Fragment>
        <div className="card rounded mt-5 mb-5 shadow">
          <div className="card-body">
            <div className="edit-save-buttons" style={{ height: "25px" }}>
              <button
                type="submit"
                className="btn btn-primary float-right"
                style={{
                  marginLeft: "10px",
                  width: "60px",
                  borderRadius: "4px",
                }}
                onClick={this.saveButton}
              >
                Save
              </button>
              <button
                type="submit"
                className="btn btn-primary float-right"
                style={{
                  marginLeft: "10px",
                  width: "70px",
                  borderRadius: "4px",
                }}
                onClick={this.props.changeToView}
              >
                Cancel
              </button>
              <button
                type="submit"
                className="btn btn-danger float-right"
                style={{
                  marginLeft: "10px",
                  width: "70px",
                  borderRadius: "4px",
                }}
                onClick={this.deleteMeter}
              >
                Delete
              </button>
            </div>
            <div>
              <div className="form-group">
                <label>Name</label>
                <input
                  type="text"
                  className="form-control"
                  name="name"
                  onChange={this.onChange}
                  value={name}
                />
              </div>
              <div className="form-group">
                <label>Utility Type</label>
                <select
                  className="form-control"
                  name="utility"
                  onChange={this.onChange}
                  value={utility}
                  disabled
                >
                  <option value="Default">{utility}</option>
                </select>
              </div>
              <div className="form-group">
                <label>Installed Date</label>
                <input
                  type="date"
                  className="form-control"
                  name="installed_date"
                  onChange={this.onChange}
                  value={installed_date}
                  disabled
                />
              </div>
              <div className="form-group">
                <label>Uninstalled Date</label>
                <input
                  type="date"
                  className="form-control"
                  name="uninstalled_date"
                  onChange={this.onChange}
                  value={uninstalled_date !== null && uninstalled_date}
                />
              </div>
            </div>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default connect(null, { createMessage, returnErrors })(
  MeterPropertiesEdit
);
