import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { withAlert } from "react-alert";

export class Alerts extends Component {
  static propTypes = {
    error: PropTypes.object.isRequired,
    message: PropTypes.object.isRequired,
  };

  componentDidUpdate(prevProps) {
    const { error, message, alert } = this.props;

    if (error != prevProps.error) {
      if (typeof error.msg === "string") alert.error(error.msg.slice(0, 100));
      if (error.msg.name) alert.error(`Name: ${error.msg.name.join()}`);
      if (error.msg.email) alert.error(`Email: ${error.msg.email.join()}`);
      if (error.msg.password)
        alert.error(`Password: ${error.msg.password.join()}`);
      if (error.msg.username)
        alert.error(`Username: ${error.msg.username.join()}`);
      if (error.msg.message)
        alert.error(`Message: ${error.msg.message.join()}`);
      if (error.msg.utility_provider)
        alert.error(Object.entries(error.msg.utility_provider[0]));
      if (error.msg.non_field_errors)
        alert.error(error.msg.non_field_errors.join());
      if (error.msg.detail) alert.error(`Error Detail: ${error.msg.detail}`);
      if (error.msg.unit_measurement)
        alert.error(`Unit Measurement: ${error.msg.unit_measurement}`);
      if (error.msg.city) alert.error(`City: ${error.msg.city}`);
      if (error.msg.state) alert.error(`State: ${error.msg.unit_measurement}`);
      if (error.msg.utility_type)
        alert.error(`Utility Type: ${error.msg.unit_measurement}`);
    }

    if (message != prevProps.message) {
      if (message.msg) alert.success(message.msg);
    }
  }

  render() {
    return <></>;
  }
}

const mapStateToProps = (state) => ({
  error: state.errors,
  message: state.messages,
});

// using withAlert - we will have access to the alert in the props
export default connect(mapStateToProps)(withAlert()(Alerts));
