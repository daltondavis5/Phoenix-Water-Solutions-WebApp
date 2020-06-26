import React from "react";
import { Switch, Route } from "react-router-dom";
import Dashboard from "./dashboard/Dashboard";
import AddProvider from "./dashboard/provider/AddProvider";
import ProviderDetails from "./dashboard/provider/ProviderDetails";
import Login from "./accounts/login";

import PrivateRoute from "./common/PrivateRoute";

function Main() {
  return (
    <main>
      <Switch>
        <Route exact path="/" component={Dashboard} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/provider/add" component={AddProvider} />
        <Route exact path="/provider/:id" component={ProviderDetails} />
      </Switch>
    </main>
  );
}

export default Main;
