import React, { Component } from "react";
import axios from 'axios'

export class ProviderDetails extends Component {

  state = {}

  componentDidMount() {
    axios.get(`/api/provider/${this.props.match.params.id}`).then((response) => {
      console.log(response.data)
      // this.setState({ utilities: response.data });
    });
  }

  render() {
    return <div>Provider Details</div>;
  }
}

export default ProviderDetails;
