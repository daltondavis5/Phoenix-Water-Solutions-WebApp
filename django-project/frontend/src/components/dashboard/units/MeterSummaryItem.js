import React, { Component } from "react";
import { Link } from "react-router-dom";

export class MeterSummaryItem extends Component {
  render() {
    const { id, name, utility, last_read_info } = this.props.meter;
    return (
      <div className="card bg-light border-dark rounded shadow">
        <div className="card-header">
          <span className="text-primary font-weight-bold">{name}</span>
          <span className="float-right">Utility: {utility}</span>
        </div>
        <div className="card-body">
          <div>
            <span className="font-weight-bold display-4 text-monospace text-success">
              {last_read_info[0]}
            </span>
          </div>
          <div>
            <span className="text-muted font-weight-lighter font-italic small">
              Last Read: {last_read_info[1]}
            </span>
            <span className="float-right">
              <Link className="text-decoration-none" to={`/meter/${id}`}>
                More info &gt;
              </Link>
            </span>
          </div>
        </div>
      </div>
    );
  }
}

export default MeterSummaryItem;
