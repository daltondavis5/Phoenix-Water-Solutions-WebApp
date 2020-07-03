import React, { Component } from "react";
import axios from "axios";

export default class MeterReads extends Component {
  state = {
    reads: [],
  };

  componentDidMount() {
    axios.get(`/api/meter/${this.props.id}/reads`).then((response) => {
      var alteredData = response.data.map((read) => {
        read.read_date = new Date(read.read_date);
        return read;
      });
      alteredData = this.sortByDate(alteredData);
      this.setState({
        reads: alteredData,
      });
    });
  }

  sortByDate = (data) => {
    return data.sort((a, b) => b.read_date - a.read_date);
  };

  convertSingleDigitToDoubleDigit = (num) => {
    return num > 9 ? "" + num : "0" + num;
  };

  formatDate = (isoDate) => {
    const time =
      this.convertSingleDigitToDoubleDigit(isoDate.getHours()) +
      ":" +
      this.convertSingleDigitToDoubleDigit(isoDate.getMinutes());
    const date =
      this.convertSingleDigitToDoubleDigit(isoDate.getMonth() + 1) +
      "-" +
      this.convertSingleDigitToDoubleDigit(isoDate.getDate()) +
      "-" +
      isoDate.getFullYear();
    return { time, date };
  };

  render() {
    return (
      <table className="table shadow">
        <caption style={{ captionSide: "top" }}>Readings</caption>
        <thead className="thead-dark">
          <tr>
            <th scope="col">Date</th>
            <th scope="col">Time</th>
            <th scope="col">Amount</th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody className="bg-light">
          {this.state.reads.map((read) => {
            const { date, time } = this.formatDate(read.read_date);
            return (
              <tr key={read.id}>
                <td style={{ width: "30%" }}>{date}</td>
                <td style={{ width: "30%" }}>{time}</td>
                <td style={{ width: "30%" }}>{read.amount}</td>
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
