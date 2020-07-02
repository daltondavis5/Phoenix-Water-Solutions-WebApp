import React, { Component } from "react";
import axios from "axios";

export default class MeterReads extends Component {
  state = {
    reads: [],
  };

  componentDidMount() {
    axios.get(`/api/meter/${this.props.id}/reads`).then((response) => {
      this.setState({
        reads: response.data,
      });
    });
  }

  render() {
    return (
      <table className="table shadow">
        <thead className="thead-dark">
          <tr>
            <th scope="col">Date</th>
            <th scope="col">Time</th>
            <th scope="col">Amount</th>
          </tr>
        </thead>
        <tbody className="bg-light">
          {this.state.reads.map((read) => {
            return (
              <tr key={read.id}>
                <td>{read.read_date.substring(0, 10)}</td>
                <td>{read.read_date.substring(11, 19)}</td>
                <td>{read.amount}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    );
  }
}
