import React, { Component } from "react";
import EditProvider from "./EditProvider";
import ViewProvider from "./ViewProvider";

export class HandleProvider extends Component {
  state = {
    mode: "viewing",
  };

  changeMode = () => {
    let currMode = this.state.mode;
    this.setState({
      mode: currMode == "viewing" ? "editing" : "viewing",
    });
  }

  render() {
    return (
      <div style={{marginTop: "20px"}}>
        {this.state.mode === "viewing" ? (
          <ViewProvider name={this.props.name} changeMode={this.changeMode} />
        ) : (
          <EditProvider
            name={this.props.name}
            updateName={this.props.updateName}
          />
        )}
      </div>
    );
  }
}

export default HandleProvider;
