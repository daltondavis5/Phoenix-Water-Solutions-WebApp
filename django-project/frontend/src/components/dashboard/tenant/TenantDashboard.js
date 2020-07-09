import React, { Component } from "react";
import axios from "axios";
import { connect } from "react-redux";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";

export class TenantDashboard extends Component {
  render() {
    const {
      first_name,
      last_name,
      email,
      account_number,
      primary_phone_number,
      secondary_phone_number,
      unit,
      move_in_date,
      move_out_date,
      credits,
      late_fee_exemption,
    } = this.props.tenant;
    return (
      <>
        <div className="card w-75 m-auto rounded shadow">
          {/* <div className="card-header">Featured</div> */}
          <div
            class="card-body"
            style={{
              backgroundImage:
                "linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%)",
            }}
          >
            <p class="card-text text-center">
              <h2 className="font-weight-bold text-dark">
                {first_name} {last_name}
              </h2>
              <p className="p-0 m-0 text-monospace">
                <i className="fa fa-envelope mr-1 text-primary"></i>
                {email}
              </p>
              <p className="p-0 m-0 text-monospace">
                <i class="fa fa-phone-square mr-1 text-primary"></i>
                {primary_phone_number}
              </p>
            </p>
          </div>
          <div class="card-body">
            <div className="row">
              <div className="col-sm-6">
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">
                    <i class="fa fa-address-book mr-1 text-primary"></i>
                    {account_number}
                  </li>
                  <li class="list-group-item">
                    <i class="fa fa-sign-in mr-1 text-primary"></i>{" "}
                    {move_in_date}
                  </li>
                  <li class="list-group-item">
                    <i class="fa fa-sign-out mr-1 text-primary"></i>{" "}
                    {move_out_date}
                  </li>
                  <li class="list-group-item">
                    <i class="fa fa-usd mr-1 text-primary"></i>{" "}
                    <span className="text-muted font-italic">
                      No credit available
                    </span>
                  </li>
                </ul>
              </div>
              <div className="border-left col-sm-6 d-flex flex-column justify-content-center align-items-center">
                <button className="btn btn-primary m-1 btn-lg w-75">
                  View Charges
                </button>
                <button className="btn btn-primary m-1 btn-lg w-75">
                  Pay Bills
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
