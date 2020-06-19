import React, { Component } from "react";
import { Link } from "react-router-dom";

export class ProviderItem extends Component {
  render() {
    return (
      <li className="list-group-item">
        <Link to={`/provider/${this.props.provider.id}`}>
          {this.props.provider.name}
        </Link>
      </li>
    );
  }
}

export default ProviderItem;
