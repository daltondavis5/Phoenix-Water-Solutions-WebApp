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
      if (typeof error.msg === "object")
        alert.error(
          Object.entries(error.msg).map((entry) => `${entry[0]}: ${entry[1]}`)
        );
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
