import React from "react";
import { Switch, Route } from "react-router-dom";
import Dashboard from "./dashboard/Dashboard";
import AddProvider from "./dashboard/provider/AddProvider";
import EditProvider from "./dashboard/provider/EditProvider";
import ProviderDetails from "./dashboard/provider/ProviderDetails";
import Login from "./accounts/login";

import PrivateRoute from "./common/PrivateRoute";

function Main() {
  // Add Private Route instead of Route if need protection like so
  // <PrivateRoute exact path="/" component={Dashboard} />
  return (
    <main>
      <Switch>
        <Route exact path="/" component={Dashboard} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/provider/add" component={AddProvider} />
        <Route exact path="/provider/edit/:id" component={EditProvider} />
        <Route exact path="/provider/:id" component={ProviderDetails} />
      </Switch>
    </main>
  );
}

export default Main;
