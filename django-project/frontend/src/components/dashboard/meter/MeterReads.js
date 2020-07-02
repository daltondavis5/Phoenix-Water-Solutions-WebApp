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
      alteredData = alteredData.sort((a, b) => b.read_date - a.read_date)
      this.setState({
        reads: alteredData,
      });
    });
  }

  formatDate = (isoDate) => {
    const time = isoDate.getHours() + ":" + isoDate.getMinutes();
    const date =
      isoDate.getMonth() +
      1 +
      "-" +
      isoDate.getDate() +
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
          </tr>
        </thead>
        <tbody className="bg-light">
          {this.state.reads.map((read) => {
            const { date, time } = this.formatDate(read.read_date);
            return (
              <tr key={read.id}>
                <td style={{width: "33%"}}>{date}</td>
                <td style={{width: "33%"}}>{time}</td>
                <td style={{width: "33%"}}>{read.amount}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    );
  }
}
