import React, { Component } from "react";

export class EditProperty extends Component {
  state = {
    name: this.props.data.name,
    address: this.props.data.address,
    zipcode: this.props.data.zipcode,
  };

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  };

  saveButton = () => {
    const data = {
      name: this.state.name,
      address: this.state.address,
      zipcode: this.state.zipcode,
    };
    this.props.saveButton(data);
  };

  render() {
    return (
      <React.Fragment>
        <div className="card" style={{ borderRadius: "10px", padding: "30px" }}>
          <div className="form-group">
            <label>Name</label>
            <input
              type="text"
              className="form-control"
              name="name"
              onChange={this.handleChange}
              value={this.state.name}
            />
          </div>
          <div className="form-group">
            <label>Address</label>
            <input
              type="text"
              className="form-control"
              name="address"
              onChange={this.handleChange}
              value={this.state.address}
            />
          </div>
          <div className="form-group">
            <label>Zipcode</label>
            <input
              type="text"
              className="form-control"
              name="zipcode"
              onChange={this.handleChange}
              value={this.state.zipcode}
            />
          </div>
        </div>
        <div
          className="edit-save-buttons"
          style={{ height: "25px", marginTop: "20px" }}
        >
          <button
            type="submit"
            className="btn btn-primary float-right"
            style={{
              marginLeft: "10px",
              width: "60px",
              borderRadius: "4px",
            }}
            onClick={this.saveButton}
          >
            Save
          </button>
          <button
            type="submit"
            className="btn btn-danger float-right"
            style={{ marginLeft: "10px", width: "70px", borderRadius: "4px" }}
            onClick={this.props.cancelButton}
          >
            Cancel
          </button>
        </div>
      </React.Fragment>
    );
  }
}

export default EditProperty;
