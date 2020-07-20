import React, { Component } from "react";
import { Link } from "react-router-dom";

export class TenantDashboardCardItem extends Component {
  render() {
    const {
      id,
      first_name,
      last_name,
      primary_email,
      primary_phone_number,
      credits,
    } = this.props.tenant;
    const {
      current_balance,
      overdue_balance,
    } = this.props.tenant.tenant_charge_info;

    return (
      <>
        <div className="card w-75 mx-auto mb-3 rounded shadow">
          <div
            className="card-body"
            style={{
              backgroundImage:
                "linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%)",
            }}
          >
            <div className="card-text text-center">
              <h2 className="font-weight-bold text-dark">
                {first_name} {last_name}
              </h2>
              <p className="p-0 m-0 text-monospace">
                <i className="fa fa-envelope mr-1 text-primary"></i>
                {primary_email}
              </p>
              <p className="p-0 m-0 text-monospace">
                <i className="fa fa-phone-square mr-1 text-primary"></i>
                {primary_phone_number}
              </p>
            </div>
          </div>
          <div className="card-body">
            <div className="row">
              <div className="col-sm-6">
                <ul className="list-group list-group-flush">
                  <li className="list-group-item">
                    <span className="text-muted font-italic">
                      Balance Due:{" "}
                    </span>
                    <i className="fa fa-usd mr-1 text-primary"></i>
                    {current_balance}
                  </li>
                  <li className="list-group-item">
                    <span className="text-muted font-italic">
                      Balance OverDue:{" "}
                    </span>
                    <i className="fa fa-usd mr-1 text-primary"></i>
                    {overdue_balance}
                  </li>
                  <li className="list-group-item">
                    <span className="text-muted font-italic">Credits: </span>
                    <i className="fa fa-usd mr-1 text-primary"></i>
                    {credits === null ? 0 : credits}
                  </li>
                </ul>
              </div>
              <div className="border-left col-sm-6 d-flex flex-column justify-content-center align-items-center">
                <button className="btn btn-primary m-1 btn-lg w-75">
                  <Link
                    className="text-decoration-none text-white"
                    to={`/tenant/${id}`}
                  >
                    View Details
                  </Link>
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

export default TenantDashboardCardItem;
