import React, { Component } from "react";
import { connect } from "react-redux";
import axios from "axios";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";
import { withRouter } from "react-router-dom";

export class TenantPropertiesEdit extends Component {
  constructor(props) {
    super(props);
    this.state = {
      id: props.tenant.id,
      first_name: props.tenant.first_name,
      last_name: props.tenant.last_name,
      primary_email: props.tenant.primary_email,
      secondary_email: props.tenant.secondary_email,
      account_number: props.tenant.account_number,
      primary_phone_number: props.tenant.primary_phone_number,
      secondary_phone_number: props.tenant.secondary_phone_number,
      move_in_date: props.tenant.move_in_date,
      move_out_date: props.tenant.move_out_date,
      credits: props.tenant.credits,
      late_fee_exemption: props.tenant.late_fee_exemption,
      unit: props.tenant.unit,
    };
  }

  static propTypes = {
    createMessage: PropTypes.func.isRequired,
    returnErrors: PropTypes.func.isRequired,
  };

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  };

  saveChanges = () => {
    const {
      id,
      first_name,
      last_name,
      primary_email,
      secondary_email,
      account_number,
      primary_phone_number,
      secondary_phone_number,
      move_in_date,
      move_out_date,
      credits,
      late_fee_exemption,
      unit,
    } = this.state;
    const body = {
      first_name,
      last_name,
      primary_email,
      secondary_email,
      account_number,
      primary_phone_number,
      secondary_phone_number,
      move_in_date,
      move_out_date,
      credits,
      late_fee_exemption,
      unit,
    };
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .put(`/api/tenant/${id}/`, JSON.stringify(body), config)
      .then((response) => {
        this.props.createMessage({ msg: "Success!" });
        this.props.updateTenant(response.data);
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  };

  deleteTenant = () => {
    const { id, unit } = this.state;
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .delete(`/api/tenant/${id}/`, config)
      .then((res) => {
        this.props.createMessage({
          msg: `Successfully deleted`,
        });
        console.log(this.props.history);
        this.props.history.push(`/unit/${unit}`);
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  };

  render() {
    const {
      first_name,
      last_name,
      primary_email,
      secondary_email,
      account_number,
      primary_phone_number,
      secondary_phone_number,
      move_in_date,
      move_out_date,
      credits,
      late_fee_exemption,
    } = this.state;
    return (
      <>
        <div className="card my-3 rounded shadow">
          <div className="card-body">
            <h4 className="card-title">
              Edit Tenant Details
              <span className="float-right">
                <button
                  type="button"
                  className="btn btn-outline-danger ml-2"
                  onClick={this.deleteTenant}
                  title="Delete Tenant"
                >
                  <i className="fa fa-trash-o"></i>
                </button>
                <button
                  type="button"
                  className="btn btn-outline-primary ml-2"
                  onClick={this.saveChanges}
                  title="Save Changes"
                >
                  <i className="fa fa-check-square-o"></i>
                </button>
                <button
                  type="button"
                  className="btn btn-outline-dark ml-2"
                  onClick={this.props.switchToView}
                  title="Close"
                >
                  <i className="fa fa-window-close-o"></i>
                </button>
              </span>
            </h4>
            <hr />
            <div className="input-group mb-3">
              <div className="input-group-prepend">
                <span className="input-group-text">First and last name</span>
              </div>
              <input
                type="text"
                className="form-control"
                name="first_name"
                onChange={this.handleChange}
                value={first_name}
                required
              />
              <input
                type="text"
                className="form-control"
                name="last_name"
                onChange={this.handleChange}
                value={last_name}
                required
              />
            </div>
            <div className="row">
              <div className="input-group mb-3 col-sm-12 col-md-6">
                <div className="input-group-prepend">
                  <span className="input-group-text">Primary Email</span>
                </div>
                <input
                  type="email"
                  className="form-control"
                  name="primary_email"
                  onChange={this.handleChange}
                  value={primary_email}
                  required
                />
              </div>
              <div className="input-group mb-3 col-sm-12 col-md-6">
                <div className="input-group-prepend">
                  <span className="input-group-text">
                    Secondary Email
                    <span className="text-muted font-italic">&nbsp;(Opt.)</span>
                  </span>
                </div>
                <input
                  type="email"
                  className="form-control"
                  name="secondary_email"
                  onChange={this.handleChange}
                  value={secondary_email}
                  placeholder="Optional Field"
                />
              </div>
            </div>
            <div className="row">
              <div className="input-group mb-3 col-sm-12 col-md-6">
                <div className="input-group-prepend">
                  <span className="input-group-text">Primary Phone Number</span>
                </div>
                <input
                  type="tel"
                  className="form-control"
                  name="primary_phone_number"
                  onChange={this.handleChange}
                  value={primary_phone_number}
                  pattern="[0-9]{10}"
                  placeholder="4801234567"
                  required
                />
              </div>
              <div className="input-group mb-3 col-sm-12 col-md -6">
                <div className="input-group-prepend">
                  <span className="input-group-text">
                    Secondary Phone Number
                    <span className="text-muted font-italic">&nbsp;(Opt.)</span>
                  </span>
                </div>
                <input
                  type="tel"
                  className="form-control"
                  name="secondary_phone_number"
                  onChange={this.handleChange}
                  value={secondary_phone_number}
                  pattern="[0-9]{10}"
                  placeholder="4801234567"
                />
              </div>
            </div>
            <div className="row">
              <div className="input-group mb-3 col-sm-12 col-md-6">
                <div className="input-group-prepend">
                  <span className="input-group-text">Move In Date</span>
                </div>
                <input
                  type="date"
                  className="form-control"
                  name="move_in_date"
                  onChange={this.handleChange}
                  value={move_in_date}
                  disabled
                />
              </div>
              <div className="input-group mb-3 col-sm-12 col-md-6">
                <div className="input-group-prepend">
                  <span className="input-group-text">
                    Move Out Date
                    <span className="text-muted font-italic">&nbsp;(Opt.)</span>
                  </span>
                </div>
                <input
                  type="date"
                  className="form-control"
                  name="move_out_date"
                  onChange={this.handleChange}
                  value={move_out_date !== null && move_out_date}
                  placeholder="Optional Field"
                />
              </div>
            </div>
            <div className="row">
              <div className="input-group mb-3 col-sm-12 col-md-6 col-lg-4">
                <div className="input-group-prepend">
                  <span className="input-group-text">
                    Account Number
                    <span className="text-muted font-italic">&nbsp;(Opt.)</span>
                  </span>
                </div>
                <input
                  type="text"
                  className="form-control"
                  name="account_number"
                  onChange={this.handleChange}
                  value={account_number}
                  placeholder="Optional Field"
                />
              </div>
              <div className="input-group mb-3 col-sm-12 col-md-6 col-lg-4">
                <div className="input-group-prepend">
                  <span className="input-group-text">
                    Credits
                    <span className="text-muted font-italic">&nbsp;(Opt.)</span>
                  </span>
                </div>
                <input
                  type="number"
                  step="any"
                  className="form-control"
                  name="credits"
                  onChange={this.handleChange}
                  value={credits}
                  placeholder="Optional Field"
                />
              </div>
              <div className="input-group mb-3 col-sm-12 col-md-12 col-lg-4">
                <div className="input-group-prepend">
                  <span className="input-group-text">
                    Late Fee Exemption
                    <span className="text-muted font-italic">&nbsp;(Opt.)</span>
                  </span>
                </div>
                <input
                  type="date"
                  className="form-control"
                  name="late_fee_exemption"
                  onChange={this.handleChange}
                  value={late_fee_exemption !== null && late_fee_exemption}
                  placeholder="Optional Field"
                />
              </div>
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default withRouter(
  connect(null, { createMessage, returnErrors })(TenantPropertiesEdit)
);
