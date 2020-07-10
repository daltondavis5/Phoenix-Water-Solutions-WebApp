import React, { Component } from "react";
import TenantProperties from "./TenantProperties";
import TenantCharges from "./TenantCharges";
import TenantPayments from "./TenantPayments";

export class TenantDetails extends Component {
  render() {
    return (
      <>
        <TenantProperties id={this.props.match.params.id} />
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
