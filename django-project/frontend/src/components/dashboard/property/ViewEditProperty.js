import React, { Component } from "react";
import EditProperty from "./EditProperty";
import ViewProperty from "./ViewProperty";

class ViewEditProperty extends Component {
  state = {
    editing: false,
  };

  changeToEdit = () => {
    this.setState({
      editing: true,
    });
  };

  saveButton = (data) => {
    this.setState({
      editing: false,
    });
    this.props.saveButton(data);
  };

  cancelButton = () => {
    this.setState({ editing: false });
  };

  render() {
    const data = {
      name: this.props.name,
      address: this.props.address,
      zipcode: this.props.zipcode,
    };
    return (
      <React.Fragment>
        {this.state.editing ? (
          <EditProperty
            data={data}
            saveButton={this.saveButton}
            cancelButton={this.cancelButton}
          />
        ) : (
          <ViewProperty data={data} changeToEdit={this.changeToEdit} />
        )}
      </React.Fragment>
    );
  }
}

export default ViewEditProperty;
