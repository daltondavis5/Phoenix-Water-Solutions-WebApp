import React, { Component } from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Dashboard from "./dashboard/Dashboard";
import { AddProviderForm } from "./AddProviderForm";

class App extends Component {
  render() {
    return (
      <React.Fragment>
        <Router>
          <Route exact path="/provider/add-provider" component={AddProviderForm} />
          <Route exact path="/provider/:id">
            <Dashboard></Dashboard>
          </Route>
        </Router>
      </React.Fragment>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
