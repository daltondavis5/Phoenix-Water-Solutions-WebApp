import React, { Component } from "react";
import axios from "axios";

export default class TenantPaymentAddModal extends Component {
  state = {
    payment_date: new Date().toISOString().slice(0, 10),
    payment_amount: "",
    payment_method: "",
    payment_method_list: [],
  };

  componentDidMount() {
    axios.get("/api/paymentmethod/").then((response) => {
      this.setState({ payment_method_list: response.data });
    });
  }

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  addTenantPayment = () => {
    const { payment_date, payment_amount, payment_method } = this.state;
    const body = {
      payment_date,
      payment_amount,
      payment_method,
    };
    this.props.addTenantPayment(body);
  };

  render() {
    const { payment_date, payment_amount, payment_method } = this.state;
    return (
      <div
        className="modal fade"
        id="tenantPaymentAddModal"
        tabIndex="-1"
        role="dialog"
      >
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title" id="modalLabel">
                Add New Tenant Payment
              </h5>
              <button
                type="button"
                className="close"
                data-dismiss="modal"
                aria-label="Close"
              >
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div className="modal-body">
              <form>
                <div className="form-group">
                  <label>Payment Date</label>
                  <input
                    type="date"
                    className="form-control"
                    name="payment_date"
                    onChange={this.onChange}
                    value={payment_date}
                  />
                </div>
                <div className="form-group">
                  <label>Payment Amount</label>
                  <input
                    type="number"
                    step="any"
                    className="form-control"
                    name="payment_amount"
                    onChange={this.onChange}
                    value={payment_amount}
                  />
                </div>
                <div className="form-group">
                  <label>Payment Method</label>
                  <select
                    className="form-control"
                    name="payment_method"
                    onChange={this.onChange}
                    value={payment_method}
                  >
                    <option value="Default">Choose a Payment method</option>
                    {this.state.payment_method_list.map((method) => {
                      return (
                        <option key={method["name"]} value={method["name"]}>
                          {method["name"]}
                        </option>
                      );
                    })}
                  </select>
                </div>
              </form>
            </div>
            <div className="modal-footer">
              <button
                type="button"
                className="btn btn-secondary"
                data-dismiss="modal"
              >
                Close
              </button>
              <button
                type="button"
                className="btn btn-primary"
                onClick={this.addTenantPayment}
                data-dismiss="modal"
              >
                Save
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
