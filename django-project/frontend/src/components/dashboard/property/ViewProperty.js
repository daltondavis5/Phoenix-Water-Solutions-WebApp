import React, { Component } from "react";

export class ViewProperty extends Component {
  render() {
    const { name, address, zipcode } = this.props.data;
    return (
      <React.Fragment>
        <div className="card" style={{ borderRadius: "10px" }}>
          <div className="card-body">
            <ul className="list-group list-group-flush">
              <li className="list-group-item">Name: {name}</li>
              <li className="list-group-item">Address: {address}</li>
              <li className="list-group-item">Zipcode: {zipcode}</li>
            </ul>
          </div>
        </div>
        <button
          type="submit"
          className="btn btn-primary float-right"
          style={{ marginLeft: "10px", marginTop: "20px", width: "100px", borderRadius: "4px" }}
          onClick={this.props.changeToEdit}
        >
          Edit Details
        </button>
      </React.Fragment>
    );
  }
}

export default ViewProperty;
