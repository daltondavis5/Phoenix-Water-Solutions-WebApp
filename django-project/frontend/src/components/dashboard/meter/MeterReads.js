import React, { Component } from "react";
import axios from "axios";
import MeterReadEditModal from "./MeterReadEditModal";
import MeterReadAddModal from "./MeterReadAddModal";
import { connect } from "react-redux";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";

export class MeterReads extends Component {
  state = {
    reads: [],
    index: 0,
    mode: "",
  };

  static propTypes = {
    createMessage: PropTypes.func.isRequired,
    returnErrors: PropTypes.func.isRequired,
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
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .post(`/api/meterread/`, JSON.stringify(data), config)
      .then((response) => {
        data["id"] = response.data.id;
        let newData = [...this.state.reads].concat(data);
        this.sortByDate(newData);
        this.setState({ reads: newData });
        this.props.createMessage({ msg: "Success!" });
        this.props.updateMeter(body);
      })
      .catch((err) => {});
  };

  editRead = (data) => {
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .put(`/api/meterread/${data.id}/`, JSON.stringify(data), config)
      .then((response) => {
        const newreads = [...this.state.reads];
        newreads.map((read) => {
          if (read.id == data.id) {
            read.amount = data.amount;
            read.read_date = data.read_date;
          }
        });
        this.setState({ reads: newreads });
        this.props.createMessage({ msg: "Success!" });
        this.props.updateMeter(body);
      })
      .catch((err) => {});
  };

  deleteRead = (id) => () => {
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .delete(`/api/meterread/${id}/`, config)
      .then((response) => {
        let filteredData = this.state.reads.filter((read) => read.id !== id);
        this.setState({ reads: filteredData, index: 0 });
        this.props.createMessage({ msg: "Success!" });
        this.props.updateMeter(body);
      })
      .catch((err) => {});
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
                <tr key={index}>
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
              editRead={this.editRead}
              deleteRead={this.deleteRead}
            />
          )
        ) : (
          <MeterReadAddModal
            meter={this.state.reads[0].meter}
            addRead={this.addRead}
          />
        )}
      </React.Fragment>
    );
  }
}

export default connect(null, { createMessage, returnErrors })(MeterReads);
