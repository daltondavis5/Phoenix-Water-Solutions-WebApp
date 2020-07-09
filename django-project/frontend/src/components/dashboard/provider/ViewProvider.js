import React, { Component } from "react";

export class ViewProvider extends Component {
  render() {
    return (
      <React.Fragment>
        <button
          type="submit"
          className="btn btn-primary float-right rounded"
          onClick={this.props.changeMode}
        >
          Edit Name
        </button>
        <h2 className="text-center">{this.props.name}</h2>
      </React.Fragment>
    );
  }
}

export default ViewProvider;
