import React, { Component } from "react";

export default class TenantChargeAddModal extends Component {
  state = {
    initial_amount: "",
    description: "",
    bill_period_end_date: "",
    due_date: "",
    priority: "",
    created: `${new Date().toISOString().slice(0, 16)}`,
    batch_id: null,
  };

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  addTenantCharge = () => {
    const {
      initial_amount,
      description,
      bill_period_end_date,
      due_date,
      priority,
      created,
      batch_id,
    } = this.state;
    const body = {
      initial_amount,
      description,
      bill_period_end_date,
      due_date,
      priority,
      created,
      batch_id,
    };
    this.props.addTenantCharge(body);
  };

  render() {
    const {
      initial_amount,
      description,
      bill_period_end_date,
      due_date,
      priority,
      created,
      batch_id,
    } = this.state;
    return (
      <div
        className="modal fade"
        id="tenantChargeAddModal"
        tabIndex="-1"
        role="dialog"
      >
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title" id="modalLabel">
                Add New Tenant Charge
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
                <div className="form-group row">
                  <label className="col-sm-3 col-form-label">Amount:</label>
                  <div className="col-sm-9">
                    <input
                      type="number"
                      step="any"
                      className="form-control"
                      name="initial_amount"
                      onChange={this.onChange}
                      value={initial_amount}
                    />
                  </div>
                </div>
                <div className="form-group row">
                  <label className="col-sm-3 col-form-label">
                    Description:
                  </label>
                  <div className="col-sm-9">
                    <input
                      type="text"
                      className="form-control"
                      name="description"
                      onChange={this.onChange}
                      value={description}
                    />
                  </div>
                </div>
                <div className="form-group row">
                  <label className="col-sm-3 col-form-label">
                    Bill Period End Date:
                  </label>
                  <div className="col-sm-9">
                    <input
                      type="date"
                      className="form-control"
                      name="bill_period_end_date"
                      onChange={this.onChange}
                      value={bill_period_end_date}
                    />
                  </div>
                </div>
                <div className="form-group row">
                  <label className="col-sm-3 col-form-label">Due Date:</label>
                  <div className="col-sm-9">
                    <input
                      type="date"
                      className="form-control"
                      name="due_date"
                      onChange={this.onChange}
                      value={due_date}
                    />
                  </div>
                </div>
                <div className="form-group row">
                  <label className="col-sm-3 col-form-label">Priority:</label>
                  <div className="col-sm-9">
                    <select
                      className="form-control"
                      name="priority"
                      onChange={this.onChange}
                      value={priority}
                    >
                      <option value="Default">Choose Priority</option>
                      {this.props.priorities.map((priority) => {
                        return (
                          <option key={priority[0]} value={priority[0]}>
                            {priority[1]}
                          </option>
                        );
                      })}
                    </select>
                  </div>
                </div>
                <div className="form-group row">
                  <label className="col-sm-3 col-form-label">
                    Created:
                    <span className="text-muted">
                      <br />
                      (UTC time)
                    </span>
                  </label>
                  <div className="col-sm-9">
                    <input
                      type="datetime-local"
                      className="form-control"
                      name="created"
                      onChange={this.onChange}
                      value={created}
                      disabled
                    />
                  </div>
                </div>
                <div className="form-group row">
                  <label className="col-sm-3 col-form-label">Batch Id:</label>
                  <div className="col-sm-9">
                    <input
                      type="number"
                      className="form-control"
                      name="batch_id"
                      onChange={this.onChange}
                      value={batch_id !== null && batch_id}
                      disabled
                    />
                  </div>
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
                onClick={this.addTenantCharge}
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
