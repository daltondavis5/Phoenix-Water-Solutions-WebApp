import React, { Component } from "react";
import MeterPropertiesView from "./MeterPropertiesView";
import MeterPropertiesEdit from "./MeterPropertiesEdit";
import axios from "axios";

class MeterProperties extends Component {
  state = {
    meter: {},
    mode: "viewing",
  };

  componentDidMount() {
    axios.get(`/api/meter/${this.props.id}`).then((response) => {
      this.setState({
        meter: response.data,
      });
    });
  }

  changeToEdit = () => {
    this.setState({ mode: "editing" });
  };

  changeToView = () => {
    this.setState({ mode: "viewing" });
  };

  updateMeter = (data) => {
    this.setState({ meter: data });
    this.changeToView();
  };

  render() {
    return (
      <React.Fragment>
        {this.state.mode === "viewing" ? (
          <MeterPropertiesView
            meter={this.state.meter}
            changeToEdit={this.changeToEdit}
          />
        ) : (
          <MeterPropertiesEdit
            meter={this.state.meter}
            changeToView={this.changeToView}
            updateMeter={this.updateMeter}
          />
        )}
      </React.Fragment>
    );
  }
}

export default MeterProperties;
