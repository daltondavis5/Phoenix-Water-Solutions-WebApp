import React, { Component } from "react";
import axios from "axios";
import { connect } from "react-redux";
import { createMessage, returnErrors } from "../../../actions/messages";
import PropTypes from "prop-types";
import TenantChargeAddModal from "./TenantChargeAddModal";
import TenantChargeEditModal from "./TenantChargeEditModal";

export class TenantCharges extends Component {
  state = {
    charges: [],
    index: 0,
    mode: "",
  };

  static propTypes = {
    createMessage: PropTypes.func.isRequired,
    returnErrors: PropTypes.func.isRequired,
  };

  componentDidMount() {
    axios.get(`/api/tenant/${this.props.id}/charges`).then((response) => {
      this.setState({ charges: response.data });
    });
  }

  viewChargeAddModal = () => {
    this.setState({ mode: "add" });
  };

  viewChargeEditModal = (index) => {
    this.setState({ index, mode: "edit" });
  };

  addTenantCharge = (body) => {
    body.tenant = this.props.id;
    console.log(body);
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .post(`/api/tenantcharge/`, JSON.stringify(body), config)
      .then((response) => {
        let charges = [...this.state.charges].concat(response.data);
        this.setState({ charges });
        this.props.createMessage({ msg: "Success!" });
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  };

  editTenantCharge = (body) => {
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .put(`/api/tenantcharge/${body.id}/`, JSON.stringify(body), config)
      .then((response) => {
        const charges = [...this.state.charges];
        charges.map((charge) => {
          if (charge.id == body.id) {
            charge.initial_amount = body.initial_amount;
            charge.remaining_amount = body.remaining_amount;
            charge.description = body.description;
            charge.bill_period_end_date = body.bill_period_end_date;
            charge.due_date = body.due_date;
            charge.priority = body.priority;
          }
        });
        this.setState({ charges });
        this.props.createMessage({ msg: "Success!" });
      })
      .catch((err) => {
        this.props.returnErrors(err.response.data, err.response.status);
      });
  };

  deleteTenantCharge = (index) => {
    const chargeId = this.state.charges[index].id;
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    axios
      .delete(`/api/tenantcharge/${chargeId}/`, config)
      .then((response) => {
        let charges = this.state.charges.filter(
          (charge) => charge.id !== chargeId
        );
        this.setState({ charges, index: 0 });
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
          <table className="table table-hover shadow-sm table-sm table-bordered text-center border-bottom">
            <caption style={{ captionSide: "top" }}>Tenant Charges</caption>
            <thead className="thead-dark">
              <tr>
                <th scope="col">Initial Amount</th>
                <th scope="col">Remaining Amount</th>
                <th scope="col">Description</th>
                <th scope="col">Bill Period End Date</th>
                <th scope="col">Due Date</th>
                <th scope="col">Priority</th>
                <th scope="col">Created</th>
                <th scope="col">Batch Id</th>
                <th scope="col">
                  <i
                    data-toggle="modal"
                    data-target="#tenantChargeAddModal"
                    className="fa fa-plus-circle fa-lg"
                    title="Add new Charge"
                    onClick={this.viewChargeAddModal}
                  ></i>
                </th>
              </tr>
            </thead>
            <tbody className="bg-light">
              {this.state.charges.map((charge, index) => {
                const {
                  initial_amount,
                  remaining_amount,
                  description,
                  bill_period_end_date,
                  due_date,
                  priority,
                  created,
                  batch_id,
                } = charge;
                return (
                  <tr key={index}>
                    <td>{initial_amount}</td>
                    <td>{remaining_amount}</td>
                    <td>{description}</td>
                    <td>{bill_period_end_date}</td>
                    <td>{due_date}</td>
                    <td>{priority}</td>
                    <td>{created}</td>
                    <td>{batch_id}</td>
                    <td style={{ width: "100px" }}>
                      <button
                        className="btn btn-outline-primary rounded btn-sm"
                        data-toggle="modal"
                        data-target="#tenantChargeEditModal"
                        title="Edit Charge"
                        onClick={() => this.viewChargeEditModal(index)}
                      >
                        <i className="fa fa-pencil-square-o"></i>
                      </button>
                      <button
                        className="btn btn-outline-danger rounded btn-sm ml-1"
                        title="Delete Charge"
                        onClick={() => this.deleteTenantCharge(index)}
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
          <TenantChargeAddModal addTenantCharge={this.addTenantCharge} />
        )}
        {this.state.mode === "edit" && (
          <TenantChargeEditModal
            charge={this.state.charges[this.state.index]}
            editTenantCharge={this.editTenantCharge}
          />
        )}
      </>
    );
  }
}

export default connect(null, { createMessage, returnErrors })(TenantCharges);
