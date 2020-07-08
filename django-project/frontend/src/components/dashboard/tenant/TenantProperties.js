import React, { Component } from "react";
import TenantPropertiesView from "./TenantPropertiesView";
import axios from "axios";

export class TenantProperties extends Component {
  state = {
    tenant: {
      id: 1,
      first_name: "Gourav",
      last_name: "Agrawal",
      primary_email: "gourav.agrawal10041996@gmail.com",
      secondary_email: null,
      account_number: null,
      primary_phone_number: "4809376076",
      secondary_phone_number: null,
      unit: 1,
      move_in_date: "Apr-10-2020",
      move_out_date: null,
      credits: null,
      late_fee_exemption: null,
    },
  };

  componentDidMount() {
    axios.get(`/api/tenant/${this.props.id}`).then((response) => {
      this.setState({
        tenant: response.data,
      });
    });
  }

  render() {
    return (
      <>
        <TenantPropertiesView tenant={this.state.tenant} />
      </>
    );
  }
}

export default TenantProperties;
