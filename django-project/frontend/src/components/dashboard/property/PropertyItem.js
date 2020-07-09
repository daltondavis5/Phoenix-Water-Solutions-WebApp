import React, { Component } from "react";
import { Link } from "react-router-dom";

export class PropertyItem extends Component {
  render() {
    return (
      <li className="list-group-item">
        <Link to={`/property/${this.props.property.id}`}>
          {this.props.property.name}
        </Link>
      </li>
    );
  }
}

export default PropertyItem;
