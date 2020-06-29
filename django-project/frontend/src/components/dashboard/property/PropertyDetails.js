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
    console.log(`/api/property/${this.props.match.params.id}`);
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
        <div class="row">
          <div class="col-3">
            <div
              class="nav flex-column nav-pills"
              id="v-pills-tab"
              role="tablist"
              aria-orientation="vertical"
            >
              <Link
                to={`/property/${this.state.id}/`}
                className="nav-link active"
                id="v-pills-home-tab"
                data-toggle="pill"
                role="tab"
                aria-controls="v-pills-home"
                aria-selected="true"
              >
                Home
              </Link>
              <Link
                to={`/property/${this.state.id}/`}
                class="nav-link"
                id="v-pills-profile-tab"
                data-toggle="pill"
                role="tab"
                aria-controls="v-pills-profile"
                aria-selected="false"
              >
                Units
              </Link>
              <Link
                class="nav-link"
                id="v-pills-messages-tab"
                data-toggle="pill"
                role="tab"
                aria-controls="v-pills-messages"
                aria-selected="false"
              >
                Add utilities
              </Link>
            </div>
          </div>
          <div class="col-9">
            <div class="tab-content" id="v-pills-tabContent">
              <div
                class="tab-pane fade show active"
                id="v-pills-home"
                role="tabpanel"
                aria-labelledby="v-pills-home-tab"
              >
                ...
              </div>
              <div
                class="tab-pane fade"
                id="v-pills-profile"
                role="tabpanel"
                aria-labelledby="v-pills-profile-tab"
              >
                ...
              </div>
              <div
                class="tab-pane fade"
                id="v-pills-messages"
                role="tabpanel"
                aria-labelledby="v-pills-messages-tab"
              >
                ...
              </div>
              <div
                class="tab-pane fade"
                id="v-pills-settings"
                role="tabpanel"
                aria-labelledby="v-pills-settings-tab"
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
