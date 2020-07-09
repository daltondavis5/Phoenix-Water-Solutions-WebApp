import React, { Component } from "react";
import MeterProperties from "./MeterProperties";
import MeterReads from "./MeterReads";
import MeterErrors from "./MeterErrors";

class MeterDetails extends Component {
  render() {
    return (
      <React.Fragment>
        <MeterProperties id={this.props.match.params.id} />
        <div className="container">
          <div className="row">
            <div className="col-sm">
              <MeterReads id={this.props.match.params.id} />
            </div>
            <div className="col-sm">
              <MeterErrors id={this.props.match.params.id} />
            </div>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default MeterDetails;
