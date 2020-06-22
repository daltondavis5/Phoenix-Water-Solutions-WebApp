import React, { Component } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

export class ProviderDetails extends Component {
  state = {
    provider: {},
  };

  componentWillMount() {
    this.getProvider();
  }

  getProvider() {
    let providerId = this.props.match.params.id;
    axios
      .get(`/api/provider/${providerId}`)
      .then((response) => {
        this.setState({ provider: response.data });
      })
      .catch((err) => console.log(err));
  }

  onDelete() {
    let providerId = this.state.provider.id;
    axios
      .delete(`/api/provider/${providerId}`)
      .then((response) => {
        // redirect to /
        this.props.history.push("/");
      })
      .catch((err) => console.log(err));
  }

  render() {
    /* const utilitys = this.state.provider.utility_provider;
    utilitys.map((utility) => console.log(utility)); */
    return (
      <div className="jumbotron mt-3">
        <h1>{this.state.provider.name}</h1>

        <Link
          className="btn btn-primary"
          to={`/provider/edit/${this.state.provider.id}`}
        >
          Edit
        </Link>

        <button onClick={this.onDelete} className="btn btn-danger float-right">
          Delete
        </button>
      </div>
    );
  }
}

export default ProviderDetails;
