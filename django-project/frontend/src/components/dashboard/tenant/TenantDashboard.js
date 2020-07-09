import React, { Component } from "react";
import axios from "axios";
import { connect } from "react-redux";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";
import TenantDashboardCardItem from "./TenantDashboardCardItem";

export class TenantDashboard extends Component {
  state = {
    first_name: "",
    last_name: "",
    primary_email: "",
    secondary_email: "",
    account_number: "",
    primary_phone_number: "",
    secondary_phone_number: "",
    move_in_date: "",
    move_out_date: null,
    credits: 0.0,
    late_fee_exemption: null,
  };

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  };

  addTenant = () => {
    let body = {
      first_name: this.state.first_name,
      last_name: this.state.last_name,
      primary_email: this.state.primary_email,
      secondary_email: this.state.secondary_email,
      account_number: this.state.account_number,
      primary_phone_number: this.state.primary_phone_number,
      secondary_phone_number: this.state.secondary_phone_number,
      move_in_date: this.state.move_in_date,
      move_out_date: this.state.move_out_date,
      credits: this.state.credits,
      late_fee_exemption: this.state.late_fee_exemption,
    };
    this.props.addTenant(body);
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
        {Object.keys(this.props.tenant).length !== 0 ? (
          <TenantDashboardCardItem tenant={this.props.tenant} />
        ) : (
          <p> No Tenants found!</p>
        )}

        <span
          className="text-primary display-4"
          style={{
            position: "fixed",
            bottom: "20px",
            right: "20px",
            cursor: "pointer",
          }}
        >
          <i
            data-toggle="modal"
            data-target="#tenantModal"
            className="fa fa-plus-circle"
          ></i>
        </span>

        <div
          className="modal fade"
          id="tenantModal"
          tabIndex="-1"
          role="dialog"
          aria-labelledby="modalLabel"
          aria-hidden="true"
        >
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title" id="modalLabel">
                  Add New Tenant
                </h5>
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
                <div>
                  <div className="input-group mb-3">
                    <div className="input-group-prepend">
                      <span className="input-group-text">
                        First and last name
                      </span>
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
                  <div className="input-group mb-3">
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
                  <div className="input-group mb-3">
                    <div className="input-group-prepend">
                      <span className="input-group-text">
                        Secondary Email
                        <span className="text-muted font-italic">
                          &nbsp;(Opt.)
                        </span>
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
                  <div className="input-group mb-3">
                    <div className="input-group-prepend">
                      <span className="input-group-text">
                        Account Number
                        <span className="text-muted font-italic">
                          &nbsp;(Opt.)
                        </span>
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
                  <div className="input-group mb-3">
                    <div className="input-group-prepend">
                      <span className="input-group-text">
                        Primary Phone Number
                      </span>
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
                  <div className="input-group mb-3">
                    <div className="input-group-prepend">
                      <span className="input-group-text">
                        Secondary Phone Number
                        <span className="text-muted font-italic">
                          &nbsp;(Opt.)
                        </span>
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
                  <div className="input-group mb-3">
                    <div className="input-group-prepend">
                      <span className="input-group-text">Move In Date</span>
                    </div>
                    <input
                      type="date"
                      className="form-control"
                      name="move_in_date"
                      onChange={this.handleChange}
                      value={move_in_date}
                      required
                    />
                  </div>
                  <div className="input-group mb-3">
                    <div className="input-group-prepend">
                      <span className="input-group-text">
                        Move Out Date
                        <span className="text-muted font-italic">
                          &nbsp;(Opt.)
                        </span>
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
                  <div className="input-group mb-3">
                    <div className="input-group-prepend">
                      <span className="input-group-text">
                        Credits
                        <span className="text-muted font-italic">
                          &nbsp;(Opt.)
                        </span>
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
                  <div className="input-group mb-3">
                    <div className="input-group-prepend">
                      <span className="input-group-text">
                        Late Fee Exemption
                        <span className="text-muted font-italic">
                          &nbsp;(Opt.)
                        </span>
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
              <div className="modal-footer">
                <button
                  type="button"
                  className="btn btn-secondary"
                  data-dismiss="modal"
                >
                  Close
                </button>
                <button
                  type="button"
                  onClick={this.addTenant}
                  className="btn btn-primary"
                  /* data-dismiss="modal" */
                >
                  Save
                </button>
              </div>
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default connect(null, { createMessage, returnErrors })(TenantDashboard);
