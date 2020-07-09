import React, { Component } from "react";

export class EditProvider extends Component {
  state = {
    name: "",
  };

  componentDidMount() {
    this.setState({
      name: this.props.name,
    });
  }

  handleChange = (e) => {
    this.setState({
      name: e.target.value,
    });
  };

  render() {
    return (
      <React.Fragment>
        <button
          type="submit"
          className="btn btn-primary float-right rounded"
          onClick={() => this.props.updateName(this.state.name)}
        >
          Save name
        </button>
        <input
          type="text"
          className="form-control mb-2"
          name="name"
          onChange={this.handleChange}
          value={this.state.name}
          style={{ width: "80%" }}
        />
      </React.Fragment>
    );
  }
}

export default EditProvider;
