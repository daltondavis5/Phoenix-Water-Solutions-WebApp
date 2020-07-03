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
      alteredData = this.sortByDate(alteredData);
      this.setState({
        errors: alteredData,
      });
    });
  }

  sortByDate = (data) => {
    return data.sort((a, b) => b.error_date - a.error_date);
  };

  convertSingleDigitToDoubleDigit = (num) => {
    return num > 9 ? "" + num : "0" + num;
  };

  formatDate = (isoDate) => {
    const date =
      this.convertSingleDigitToDoubleDigit(isoDate.getMonth() + 1) +
      "-" +
      this.convertSingleDigitToDoubleDigit(isoDate.getDate()) +
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
            <th
              style={{
                textAlign: "center",
                cursor: "pointer",
              }}
              scope="col"
              scope="col"
            >
              <i
                data-toggle="modal"
                data-target="#meterModal"
                className="fa fa-plus-circle fa-lg"
              ></i>
            </th>
          </tr>
        </thead>
        <tbody className="bg-light">
          {this.state.errors.map((error) => {
            return (
              <tr key={error.id}>
                <td style={{ width: "25%" }}>
                  {this.formatDate(new Date(error.error_date))}
                </td>
                <td style={{ width: "25%" }}>{error.description}</td>
                <td style={{ width: "25%" }}>{error.repair_date}</td>
                <td style={{ width: "10%" }}>
                  <button className="btn btn-primary float-right rounded">
                    Edit
                  </button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    );
  }
}
