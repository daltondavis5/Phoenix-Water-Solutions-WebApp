import React, { Component } from "react";
import { connect } from "react-redux";
import axios from "axios";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";

export class PropertyDetails extends Component {
  static propTypes = {
    createMessage: PropTypes.func.isRequired,
    returnErrors: PropTypes.func.isRequired,
  };

  state = {
    id: "",
    name: "",
    street_address: "",
    zip_code: "",
    attribute: "",
    city_utility: [],
  };

  componentDidMount() {
    axios
      .get(`/api/property/${this.props.match.params.id}`)
      .then((response) => {
        const {
          id,
          name,
          street_address,
          zip_code,
          attribute,
          city_utility,
        } = response.data;
        this.setState({
          id,
          name,
          street_address,
          zip_code,
          attribute,
          city_utility,
        });
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  }

  render() {
    return (
      <React.Fragment>
        <h2 className="text-center">{this.state.name}</h2>
        <h2 className="text-center">{this.state.street_address}</h2>
        <div className="row">
          <div className="col-3">
            <div
              className="nav flex-column nav-pills"
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
                id="v-pills-units-tab"
                data-toggle="pill"
                href="#v-pills-units"
                role="tab"
                aria-controls="v-pills-units"
                aria-selected="false"
              >
                Units
              </a>
              <a
                className="nav-link"
                id="v-pills-utilities-tab"
                data-toggle="pill"
                href="#v-pills-utilities"
                role="tab"
                aria-controls="v-pills-utilities"
                aria-selected="false"
              >
                Utilities
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
                Hello
              </div>
              <div
                className="tab-pane fade"
                id="v-pills-units"
                role="tabpanel"
                aria-labelledby="v-pills-units-tab"
              >
                Hey
              </div>
              <div
                className="tab-pane fade"
                id="v-pills-utilities"
                role="tabpanel"
                aria-labelledby="v-pills-utilities-tab"
              >
                ...
              </div>
            </div>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default connect(null, { createMessage, returnErrors })(PropertyDetails);
