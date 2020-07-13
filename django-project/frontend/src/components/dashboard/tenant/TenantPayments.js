import React, { Component } from "react";
import axios from "axios";
import { connect } from "react-redux";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";
import TenantPaymentAddModal from "./TenantPaymentAddModal";

export class TenantPayments extends Component {
  state = {
    payments: [],
    index: 0,
    adding: false,
    toggleSort: false,
  };

  static propTypes = {
    createMessage: PropTypes.func.isRequired,
    returnErrors: PropTypes.func.isRequired,
  };

  componentDidMount() {
    axios.get(`/api/tenant/${this.props.id}/payments`).then((response) => {
      this.setState({ payments: response.data });
    });
  }

  viewPaymentAddModal = () => {
    this.setState({ adding: true });
  };

  addTenantPayment = (body) => {
    body.tenant = this.props.id;
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .post(`/api/payment/`, JSON.stringify(body), config)
      .then((response) => {
        let payments = [...this.state.payments].concat(response.data);
        this.setState({ payments, adding: false });
        this.props.createMessage({ msg: "Success!" });
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  };

  deleteTenantPayment = (index) => {
    let paymentId = this.state.payments[index].id;
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .delete(`/api/payment/${paymentId}/`, config)
      .then((response) => {
        let payments = this.state.payments.filter(
          (payment) => payment.id !== paymentId
        );
        this.setState({ payments, index: 0 });
        this.props.createMessage({ msg: "Success!" });
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  };

  sortByPaymentDate = () => {
    const payments = [...this.state.payments];
    const sorted_payments = payments.sort((a, b) =>
      this.state.toggleSort
        ? new Date(b.payment_date) - new Date(a.payment_date)
        : new Date(a.payment_date) - new Date(b.payment_date)
    );
    const toggleSort = !this.state.toggleSort;
    this.setState({ payments: sorted_payments, toggleSort });
  };

  render() {
    return (
      <>
        <div className="table-responsive">
          <table className="table table-bordered shadow-sm table-sm table-hover text-center border-bottom">
            <caption style={{ captionSide: "top" }}>Tenant Payments</caption>
            <thead className="thead-dark">
              <tr>
                <th scope="col">
                  Payment Date{" "}
                  <i
                    className="fa fa-sort"
                    role="button"
                    onClick={this.sortByPaymentDate}
                  ></i>
                </th>
                <th scope="col">Payment Amount</th>
                <th scope="col">Applied Amount</th>
                <th scope="col">Payment Method</th>
                <th scope="col">
                  <i
                    data-toggle="modal"
                    data-target="#tenantPaymentAddModal"
                    className="fa fa-plus-circle fa-lg"
                    title="Add new Payment"
                    role="button"
                    onClick={this.viewPaymentAddModal}
                  ></i>
                </th>
              </tr>
            </thead>
            <tbody className="bg-light">
              {this.state.payments.map((payment, index) => {
                const {
                  payment_date,
                  payment_amount,
                  applied_amount,
                  payment_method,
                } = payment;
                return (
                  <tr key={index}>
                    <td>{payment_date}</td>
                    <td>{payment_amount}</td>
                    <td>{applied_amount}</td>
                    <td>{payment_method}</td>
                    <td style={{ width: "100px" }}>
                      <button
                        className="btn btn-outline-danger rounded btn-sm ml-1"
                        title="Delete Payment"
                        onClick={() => this.deleteTenantPayment(index)}
                      >
                        <i className="fa fa-trash-o"></i>
                      </button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>

        {this.state.adding && (
          <TenantPaymentAddModal addTenantPayment={this.addTenantPayment} />
        )}
      </>
    );
  }
}

export default connect(null, { createMessage, returnErrors })(TenantPayments);
