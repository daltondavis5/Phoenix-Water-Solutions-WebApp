import React, { Component } from "react";

export default class TenantChargeAddModal extends Component {
  state = {
    initial_amount: 0.0,
    remaining_amount: 0.0,
    description: "",
    bill_period_end_date: "",
    due_date: "",
    priority: 0,
    created: "",
    batch_id: 0,
  };

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  addTenantCharge = () => {
    const {
      initial_amount,
      remaining_amount,
      description,
      bill_period_end_date,
      due_date,
      priority,
      created,
      batch_id,
    } = this.state;
    const body = {
      initial_amount,
      remaining_amount,
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
      remaining_amount,
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
                  <label className="col-sm-3 col-form-label">
                    Initial Amount:
                  </label>
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
                    Remaining Amount:
                  </label>
                  <div className="col-sm-9">
                    <input
                      type="number"
                      step="any"
                      className="form-control"
                      name="remaining_amount"
                      onChange={this.onChange}
                      value={remaining_amount}
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
                    <input
                      type="number"
                      className="form-control"
                      name="priority"
                      onChange={this.onChange}
                      min="0"
                      max="2"
                      value={priority}
                    />
                  </div>
                </div>
                <div className="form-group row">
                  <label className="col-sm-3 col-form-label">Created:</label>
                  <div className="col-sm-9">
                    <input
                      type="datetime-local"
                      className="form-control"
                      name="created"
                      onChange={this.onChange}
                      value={created}
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
                      value={batch_id}
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
                /* data-dismiss="modal" */
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
