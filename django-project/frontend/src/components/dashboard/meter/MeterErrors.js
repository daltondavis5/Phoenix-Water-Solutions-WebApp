import React, { Component } from "react";
import axios from "axios";
import MeterErrorEditModal from "./MeterErrorEditModal";
import MeterErrorAddModal from "./MeterErrorAddModal";

export default class MeterErrors extends Component {
  state = {
    errors: [],
    index: 0,
    mode: "",
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

  handleEditShow = (index) => () => {
    this.setState({ index, mode: "edit" });
  };

  handleAddShow = () => {
    this.setState({ mode: "add" });
  };

  render() {
    return (
      <React.Fragment>
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
                  data-target="#meterErrorAdd"
                  className="fa fa-plus-circle fa-lg"
                  onClick={this.handleAddShow}
                ></i>
              </th>
            </tr>
          </thead>
          <tbody className="bg-light">
            {this.state.errors.map((error, index) => {
              return (
                <tr key={error.id}>
                  <td style={{ width: "30%" }}>
                    {this.formatDate(new Date(error.error_date))}
                  </td>
                  <td style={{ width: "30%" }}>{error.description}</td>
                  <td style={{ width: "30%" }}>{error.repair_date}</td>
                  <td style={{ width: "10%" }}>
                    <button
                      className="btn btn-primary float-right rounded"
                      data-toggle="modal"
                      data-target="#meterErrorEdit"
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
          this.state.errors.length > 0 && (
            <MeterErrorEditModal
              description={this.state.errors[this.state.index].description}
              id={this.state.errors[this.state.index].id}
              meter={this.state.errors[this.state.index].meter}
              error_date={this.formatDate(
                new Date(this.state.errors[this.state.index].repair_date)
              )}
              repair_date={this.state.errors[this.state.index].repair_date}
            />
          )
        ) : (
          <MeterErrorAddModal addRead={this.addRead} />
        )}
      </React.Fragment>
    );
  }
}
