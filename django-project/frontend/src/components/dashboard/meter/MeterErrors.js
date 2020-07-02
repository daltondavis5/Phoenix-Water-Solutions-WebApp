import React, { Component } from "react";
import axios from "axios";

export default class MeterErrors extends Component {
  state = {
    errors: [],
  };

  componentDidMount() {
    axios.get(`/api/meter/${this.props.id}/errors`).then((response) => {
      var alteredData = response.data.map((error) => {
        error.error_date = new Date(error.error_date);
        return error;
      });
      alteredData = alteredData.sort((a, b) => b.error_date - a.error_date);
      this.setState({
        errors: alteredData,
      });
    });
  }

  formatDate = (isoDate) => {
    const date =
      isoDate.getMonth() +
      1 +
      "-" +
      isoDate.getDate() +
      "-" +
      isoDate.getFullYear();
    return date;
  };

  render() {
    return (
      <table className="table shadow">
        <caption style={{ captionSide: "top" }}>Errors</caption>
        <thead className="thead-dark">
          <tr>
            <th scope="col">Date</th>
            <th scope="col">Description</th>
            <th scope="col">Repair Date</th>
          </tr>
        </thead>
        <tbody className="bg-light">
          {this.state.errors.map((error) => {
            return (
              <tr key={error.id}>
                <td style={{ width: "33%" }}>
                  {this.formatDate(new Date(error.error_date))}
                </td>
                <td style={{ width: "33%" }}>{error.description}</td>
                <td style={{ width: "33%" }}>{error.repair_date}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    );
  }
}
