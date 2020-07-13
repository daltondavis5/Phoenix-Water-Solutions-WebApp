import React, { Component } from "react";
import axios from "axios";
import { connect } from "react-redux";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";
import MeterDashboard from "./MeterDashboard";
import TenantDashboard from "../tenant/TenantDashboard";

export class UnitDetails extends Component {
  static propTypes = {
    createMessage: PropTypes.func.isRequired,
    returnErrors: PropTypes.func.isRequired,
  };

  state = {
    unit: {},
    meters: [],
    utilities: [],
    tenants: [],
  };

  componentDidMount() {
    axios
      .get(`/api/unit/${this.props.match.params.id}`)
      .then((response) => {
        this.setState({
          unit: response.data,
        });
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });

    axios.get("/api/utility/").then((response) => {
      this.setState({ utilities: response.data });
    });

    this.getMetersWithinUnitsList();
    this.getTenantsWithinUnitsList();
  }

  getMetersWithinUnitsList = () => {
    axios
      .get(`/api/unit/${this.props.match.params.id}/meters`)
      .then((response) => {
        this.setState({
          meters: response.data,
        });
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  };

  getTenantsWithinUnitsList = () => {
    axios
      .get(`/api/unit/${this.props.match.params.id}/tenants`)
      .then((response) => {
        this.setState({
          tenants: response.data,
        });
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  };

  addMeter = (body) => {
    body.unit = this.state.unit.id;
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };

    axios
      .post("/api/meter/", JSON.stringify(body), config)
      .then((response) => {
        this.getMetersWithinUnitsList();
        this.props.createMessage({ msg: "Success!" });
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  };

  addTenant = (body) => {
    body.unit = this.state.unit.id;
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };

    axios
      .post("/api/tenant/", JSON.stringify(body), config)
      .then((response) => {
        this.getTenantsWithinUnitsList();
        this.props.createMessage({ msg: "Success!" });
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  };

  render() {
    const { name } = this.state.unit;
    return (
      <>
        <h2 className="text-center mt-3 border-bottom">{name}</h2>
        <div style={{ marginTop: "30px" }}>
          <div className="row">
            <div className="col-3">
              <div
                className="nav flex-column nav-pills bg-white"
                id="v-pills-tab"
                role="tablist"
                aria-orientation="vertical"
              >
                <a
                  className="nav-link active"
                  id="v-pills-home-tab"
                  data-toggle="pill"
                  href="#v-pills-home"
                  role="tab"
                  aria-controls="v-pills-home"
                  aria-selected="true"
                >
                  Home
                </a>
                <a
                  className="nav-link"
                  id="v-pills-meters-tab"
                  data-toggle="pill"
                  href="#v-pills-meters"
                  role="tab"
                  aria-controls="v-pills-meters"
                  aria-selected="false"
                >
                  Meters
                </a>
                <a
                  className="nav-link"
                  id="v-pills-tenants-tab"
                  data-toggle="pill"
                  href="#v-pills-tenants"
                  role="tab"
                  aria-controls="v-pills-tenants"
                  aria-selected="false"
                >
                  Tenants
                </a>
              </div>
            </div>
            <div className="col-9">
              <div className="tab-content" id="v-pills-tabContent">
                <div
                  className="tab-pane fade show active"
                  id="v-pills-home"
                  role="tabpanel"
                  aria-labelledby="v-pills-home-tab"
                >
                  Home
                </div>
                <div
                  className="tab-pane fade"
                  id="v-pills-meters"
                  role="tabpanel"
                  aria-labelledby="v-pills-meters-tab"
                >
                  <MeterDashboard
                    meters={this.state.meters}
                    utilities={this.state.utilities}
                    addMeter={this.addMeter}
                  />
                </div>
                <div
                  className="tab-pane fade"
                  id="v-pills-tenants"
                  role="tabpanel"
                  aria-labelledby="v-pills-tenants-tab"
                >
                  <TenantDashboard
                    tenants={this.state.tenants}
                    addTenant={this.addTenant}
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default connect(null, { createMessage, returnErrors })(UnitDetails);
