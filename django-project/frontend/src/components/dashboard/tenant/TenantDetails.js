import React, { Component } from "react";
import TenantProperties from "./TenantProperties";

export class TenantDetails extends Component {
  render() {
    return (
      <>
        <TenantProperties id={this.props.match.params.id} />
      </>
    );
  }
}

export default TenantDetails;
