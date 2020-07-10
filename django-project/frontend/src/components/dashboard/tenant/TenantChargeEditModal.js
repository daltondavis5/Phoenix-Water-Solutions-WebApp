import React, { Component } from "react";

export default class TenantChargeEditModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      id: props.charge.id,
      initial_amount: props.charge.initial_amount,
      remaining_amount: props.charge.remaining_amount,
      description: props.charge.description,
      bill_period_end_date: props.charge.bill_period_end_date,
      due_date: props.charge.due_date,
      priority: props.charge.priority,
      created: props.charge.created,
      batch_id: props.charge.batch_id,
      tenant: props.charge.tenant,
    };
  }

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  editTenantCharge = () => {
    const {
      id,
      initial_amount,
      remaining_amount,
      description,
      bill_period_end_date,
      due_date,
      priority,
      created,
      batch_id,
      tenant,
    } = this.state;
    const body = {
      id,
      initial_amount,
      remaining_amount,
      description,
      bill_period_end_date,
      due_date,
      priority,
      created,
      batch_id,
      tenant,
    };
    this.props.editTenantCharge(body);
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
        id="tenantChargeEditModal"
        tabIndex="-1"
        role="dialog"
      >
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title" id="modalLabel">
                Edit Tenant Charge
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
                onClick={this.editTenantCharge}
                /* data-dismiss="modal" */
              >
                Save changes
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
