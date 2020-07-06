import React, { Component } from "react";
import axios from "axios";
import MeterReadEditModal from "./MeterReadEditModal";
import MeterReadAddModal from "./MeterReadAddModal";

export default class MeterReads extends Component {
  state = {
    reads: [],
    index: 0,
    mode: "",
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

  handleEditShow = (index) => () => {
    this.setState({ index, mode: "edit" });
  };

  handleAddShow = () => {
    this.setState({ mode: "add" });
  };

  addRead = (data) => {
    const { meter, time, date, amount } = data;
    console.log(new Date(date, time))
  };

  render() {
    return (
      <React.Fragment>
        <table className="table shadow">
          <caption style={{ captionSide: "top" }}>Readings</caption>
          <thead className="thead-dark">
            <tr>
              <th>Date</th>
              <th scope="col">Time</th>
              <th scope="col">Amount</th>
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
                  data-target="#meterReadAdd"
                  className="fa fa-plus-circle fa-lg"
                  onClick={this.handleAddShow}
                ></i>
              </th>
            </tr>
          </thead>
          <tbody className="bg-light">
            {this.state.reads.map((read, index) => {
              const { date, time } = this.formatDate(read.read_date);
              return (
                <tr key={read.id}>
                  <td style={{ width: "30%" }}>{date}</td>
                  <td style={{ width: "30%" }}>{time}</td>
                  <td style={{ width: "30%" }}>{read.amount}</td>
                  <td style={{ width: "10%" }}>
                    <button
                      className="btn btn-primary float-right rounded"
                      data-toggle="modal"
                      data-target="#meterReadEdit"
                      onClick={this.handleEditShow(index, "edit")}
                    >
                      Edit
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
        {this.state.mode !== "add" ? (
          this.state.reads.length > 0 && (
            <MeterReadEditModal
              amount={this.state.reads[this.state.index].amount}
              id={this.state.reads[this.state.index].id}
              meter={this.state.reads[this.state.index].meter}
              amount={this.state.reads[this.state.index].amount}
              isoDate={this.formatDate(
                this.state.reads[this.state.index].read_date
              )}
              mode={this.state.mode}
            />
          )
        ) : (
          <MeterReadAddModal addRead={this.addRead} />
        )}
      </React.Fragment>
    );
  }
}
