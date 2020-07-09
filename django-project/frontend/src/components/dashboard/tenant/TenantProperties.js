import React, { Component } from "react";
import axios from "axios";
import TenantPropertiesView from "./TenantPropertiesView";
import TenantPropertiesEdit from "./TenantPropertiesEdit";

export class TenantProperties extends Component {
  state = {
    tenant: {},
    editing: false,
  };

  componentDidMount() {
    axios.get(`/api/tenant/${this.props.id}`).then((response) => {
      this.setState({
        tenant: response.data,
      });
    });
  }

  switchToView = () => {
    this.setState({ editing: false });
  };

  switchToEdit = () => {
    this.setState({ editing: true });
  };

  updateTenant = (tenant) => {
    this.setState({ tenant, editing: false });
  };

  render() {
    return (
      <>
        {Object.keys(this.state.tenant).length !== 0 ? (
          this.state.editing ? (
            <TenantPropertiesEdit
              tenant={this.state.tenant}
              switchToView={this.switchToView}
              updateTenant={this.updateTenant}
            />
          ) : (
            <TenantPropertiesView
              tenant={this.state.tenant}
              switchToEdit={this.switchToEdit}
            />
          )
        ) : (
          <p>No Tenants found!</p>
        )}
      </>
    );
  }
}

export default TenantProperties;
