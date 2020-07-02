import React, { Component } from "react";
import axios from "axios";
import { connect } from "react-redux";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";
import UnitMeters from "./UnitMeters";
import MeterDashboard from "./MeterDashboard";

export class UnitDetails extends Component {
  static propTypes = {
    createMessage: PropTypes.func.isRequired,
    returnErrors: PropTypes.func.isRequired,
  };

  state = {
    unit: {},
    meters: [],
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

    axios
      .get(`/api/unit/${this.props.match.params.id}/meters`)
      .then((response) => {
        var alteredData = response.data.map((data) => {
          data.mode = "viewing";
          return data;
        });
        this.setState({
          meters: alteredData,
        });
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  }

  changeToEdit = (index) => () => {
    let meters = [...this.state.meters];
    meters[index]["mode"] = "editing";
    this.setState({
      meters,
    });
  };

  handleChange = (index) => (e) => {
    let meters = [...this.state.meters];
    meters[index][e.target.name] = e.target.value;
    this.setState({
      meters,
    });
  };

  saveButton = (index) => {
    let meter = this.state.meters[index];
    const body = {
      name: meter.name,
      utility_type: meter.utility_type,
      installed_date: meter.installed_date,
      uninstalled_date: meter.uninstalled_date,
      unit_name: meter.unit_name,
    };
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };

    if (meter.mode == "adding") {
      axios
        .post("/api/meter/", JSON.stringify(body), config)
        .then((response) => {
          meter["id"] = response.data.id;
          this.props.createMessage({ msg: "Success!" });
        })
        .catch((err) => {
          this.props.returnErrors(err.response.data, err.response.status);
        });
    }
    if (meter.mode == "editing") {
      axios
        .put(`/api/meter/${meter["id"]}/`, JSON.stringify(body), config)
        .then((response) => {
          this.props.createMessage({ msg: "Success!" });
        })
        .catch((err) => {
          this.props.returnErrors(err.response.data, err.response.status);
        });
    }
    let meters = [...this.state.meters];
    meters[index]["mode"] = "viewing";
    this.setState({
      meter: meters,
    });
  };

  deleteButton = (index) => {
    let meter = this.state.meters[index];
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    if (meter.mode == "editing") {
      axios.delete(`/api/meter/${meter["id"]}/`, config).then((response) => {});
    }
    let meters = [
      ...this.state.meters.slice(0, index),
      ...this.state.meters.slice(index + 1),
    ];
    this.setState({
      meters,
    });
  };

  addMeter = (e) => {
    e.preventDefault();
    let meters = this.state.meters.concat([
      {
        installed_date: "",
        mode: "adding",
        name: "",
        uninstalled_date: "",
        unit_name: this.state.unit.name,
        utility_type: "",
      },
    ]);
    this.setState({
      meters,
    });
  };

  render() {
    const { id, name } = this.state.unit;
    return (
      <>
        <h2 className="text-center mt-3">{name}</h2>
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
                  {/* <UnitMeters
                    meters={this.state.meters}
                    unit_id={id}
                    changeToEdit={this.changeToEdit}
                    onChange={this.handleChange}
                    saveButton={this.saveButton}
                    deleteButton={this.deleteButton}
                    addMeter={this.addMeter}
                  /> */}
                  <MeterDashboard meters={this.state.meters} />
                </div>
                <div
                  className="tab-pane fade"
                  id="v-pills-tenants"
                  role="tabpanel"
                  aria-labelledby="v-pills-tenants-tab"
                >
                  Tenant Details
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
