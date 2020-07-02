import React, { Component } from "react";
import axios from "axios";

export default class MeterErrors extends Component {
  state = {
    errors: [],
  };

  componentDidMount() {
    axios.get(`/api/meter/${this.props.id}/errors`).then((response) => {
      this.setState({
        errors: response.data,
      });
    });
  }

  render() {
    return (
      <table className="table shadow">
        <thead className="thead-dark">
          <tr>
            <th scope="col">Date</th>
            <th scope="col">Description</th>
            <th scope="col">Repair Date</th>
          </tr>
        </thead>
        <tbody>
          {this.state.errors.map((error) => {
            return (
              <tr key={error.id}>
                <td>{error.error_date}</td>
                <td>{error.description}</td>
                <td>{error.repair_date}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    );
  }
}
