import React, { Component } from "react";
import MeterEdit from "./MeterEdit";
import MeterView from "./MeterView";

class UnitMeters extends Component {
  state = {
    adding: false,
  };

  saveButton = (index) => () => {
    this.setState({adding: false})
    this.props.saveButton(index);
  }

  deleteButton = (index) => () => {
    this.setState({adding: false})
    this.props.deleteButton(index);
  }

  addMeter = (e) => {
    this.setState({adding: true})
    this.props.addMeter(e);
  }

  render() {
    return (
      <React.Fragment>
        {this.props.meters.map((meter, index) => {
          return meter.mode === "viewing" ? (
            <MeterView
              key={index}
              meter={meter}
              changeToEdit={this.props.changeToEdit(index)}
            />
          ) : (
            // editing or adding
            <MeterEdit
              key={index}
              meter={meter}
              onChange={this.props.onChange(index)}
              saveButton={this.saveButton(index)}
              deleteButton={this.deleteButton(index)}
            />
          );
        })}
        {!this.state.adding && (
          <div className="form-group" style={{ marginTop: "20px" }}>
            <button
              onClick={this.addMeter}
              className="btn btn-outline-secondary"
              style={{ borderRadius: "4px" }}
            >
              Add New Meter
            </button>
          </div>
        )}
      </React.Fragment>
    );
  }
}

export default UnitMeters;
