import React, { Component } from "react";
import { connect } from "react-redux";
import axios from "axios";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";

export class PropertyDetails extends Component {
  state = {
    
  };

  static propTypes = {
    createMessage: PropTypes.func.isRequired,
    returnErrors: PropTypes.func.isRequired,
  };

  componentDidMount() {
    axios
      .get(`/api/property/${this.props.match.params.id}`)
      .then((response) => {
        var alteredData = response.data.utility_property.map((data) => {
          data.mode = "viewing";
          return data;
        });
        this.setState({
          name: response.data.name,
          utility_property: alteredData,
        });
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
    // TODO: Is setting the state again necessary??
    this.setState((prevState) => {
      prevState.utility_property.map(
        (utility_property_item) => (utility_property_item["mode"] = "viewing")
      );
    });
  }

  render() {
    return (
      <React.Fragment>
        
      </React.Fragment>
    );
  }
}

export default connect(null, { createMessage, returnErrors })(PropertyDetails);
