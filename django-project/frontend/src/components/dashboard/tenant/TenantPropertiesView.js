import React, { Component } from "react";

export class TenantPropertiesView extends Component {
  render() {
    const {
      id,
      first_name,
      last_name,
      primary_email,
      secondary_email,
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
        <div
          className="card my-3 rounded shadow"
          style={{ borderLeft: "5px solid #2780E3" }}
        >
          <div className="card-body">
            <h4 className="card-title text-center">
              Tenant Details
              <sup>
                <i
                  className="fa fa-pencil-square-o text-primary ml-2"
                  role="button"
                  onClick={this.props.switchToEdit}
                ></i>
              </sup>
            </h4>
            <hr />
            <div className="card-text">
              <p className="mb-1">
                Name:{" "}
                <strong>
                  {first_name} {last_name}
                </strong>
              </p>
              <p className="mb-1">
                Email:{" "}
                <strong>
                  {primary_email}{" "}
                  {secondary_email !== null && secondary_email !== ""
                    ? ` | ${secondary_email}`
                    : ""}
                </strong>
              </p>
              <p className="mb-1">
                Contact Number:{" "}
                <strong>
                  {primary_phone_number}{" "}
                  {secondary_phone_number !== null &&
                  secondary_phone_number !== ""
                    ? ` | ${secondary_phone_number}`
                    : ""}
                </strong>
              </p>
            </div>
            <hr />
            <div className="card-text">
              <p className="mb-1">
                Unit Id: <strong>{unit}</strong>
              </p>
              <p className="mb-1">
                Move In Date: <strong>{move_in_date}</strong>
              </p>
              <p className="mb-1">
                Move Out Date:{" "}
                <strong>
                  {move_out_date !== null ? move_out_date : "Unavailable"}
                </strong>
              </p>
            </div>
            <hr />
            <div className="card-text">
              <p className="mb-1">
                Account Number:{" "}
                <strong>
                  {account_number !== null ? account_number : "Unavailable"}
                </strong>
              </p>
              <p className="mb-1">
                Credits:{" "}
                <strong>{credits !== null ? credits : "Unavailable"}</strong>
              </p>
              <p className="mb-1">
                Late Fee Exemption:{" "}
                <strong>
                  {late_fee_exemption !== null
                    ? late_fee_exemption
                    : "Unavailable"}
                </strong>
              </p>
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default TenantPropertiesView;
