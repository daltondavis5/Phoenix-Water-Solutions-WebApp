import React, { Component } from "react";
import TenantProperties from "./TenantProperties";
import TenantCharges from "./TenantCharges";
import TenantPayments from "./TenantPayments";

export class TenantDetails extends Component {
  render() {
    return (
      <>
        <div className="row mt-3">
          <div className="col-sm-12 col-lg-9">
            <TenantProperties id={this.props.match.params.id} />
          </div>
          <div className="col-sm-12 col-lg-3 d-flex flex-column">
            <div
              className="card card-body shadow text-white mb-2 justify-content-center align-items-center"
              style={{
                borderRadius: "7%",
                backgroundColor: "rgba(251, 116, 84, 0.9)",
              }}
            >
              <h1 className="display-4">
                <i class="fa fa-usd"></i>
                <strong>785</strong>
              </h1>
              <p>Current Balance</p>
            </div>
            <div
              className="card card-body shadow text-white justify-content-center align-items-center"
              style={{
                borderRadius: "7%",
                backgroundColor: "rgba(248, 164, 73, 0.9)",
              }}
            >
              <h1 className="display-4">
                <i class="fa fa-usd"></i>
                <strong>356</strong>
              </h1>
              <p>Overdue Balance</p>
            </div>
          </div>
        </div>
        <div className="row">
          <div className="col-sm-12">
            <TenantCharges id={this.props.match.params.id} />
          </div>
          <div className="col-sm-12">
            <TenantPayments id={this.props.match.params.id} />
          </div>
        </div>
      </>
    );
  }
}

export default TenantDetails;
