import React, { Component } from "react";
import axios from "axios";
import { connect } from "react-redux";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";
import TenantPaymentAddModal from "./TenantPaymentAddModal";
import TenantPaymentEditModal from "./TenantPaymentEditModal";

export class TenantPayments extends Component {
  state = {
    payments: [],
    index: 0,
    mode: "",
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
    this.setState({ mode: "add" });
  };

  viewPaymentEditModal = (index) => {
    this.setState({ index, mode: "edit" });
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
        this.setState({ payments });
        this.props.createMessage({ msg: "Success!" });
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  };

  editTenantPayment = (body) => {
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .put(`/api/payment/${body.id}/`, JSON.stringify(body), config)
      .then((response) => {
        const payments = [...this.state.payments];
        payments.map((payment) => {
          if (payment.id == body.id) {
            payment.payment_date = body.payment_date;
            payment.payment_amount = body.payment_amount;
            payment.applied_amount = body.applied_amount;
            payment.payment_method = body.payment_method;
          }
        });
        this.setState({ payments });
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

  render() {
    return (
      <>
        <div className="table-responsive">
          <table className="table table-bordered shadow-sm table-sm table-hover text-center border-bottom">
            <caption style={{ captionSide: "top" }}>Tenant Payments</caption>
            <thead className="thead-dark">
              <tr>
                <th scope="col">Payment Date</th>
                <th scope="col">Payment Amount</th>
                <th scope="col">Applied Amount</th>
                <th scope="col">Payment Method</th>
                <th scope="col">
                  <i
                    data-toggle="modal"
                    data-target="#tenantPaymentAddModal"
                    className="fa fa-plus-circle fa-lg"
                    title="Add new Payment"
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
                        className="btn btn-outline-primary rounded btn-sm"
                        data-toggle="modal"
                        data-target="#tenantPaymentEditModal"
                        title="Edit Payment"
                        onClick={() => this.viewPaymentEditModal(index)}
                      >
                        <i className="fa fa-pencil-square-o"></i>
                      </button>
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

        {this.state.mode === "add" && (
          <TenantPaymentAddModal addTenantPayment={this.addTenantPayment} />
        )}
        {this.state.mode === "edit" && (
          <TenantPaymentEditModal
            payment={this.state.payments[this.state.index]}
            editTenantPayment={this.editTenantPayment}
          />
        )}
      </>
    );
  }
}

export default connect(null, { createMessage, returnErrors })(TenantPayments);
