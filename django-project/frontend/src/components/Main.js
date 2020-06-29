import React from "react";
import { Switch, Route } from "react-router-dom";
import Dashboard from "./dashboard/Dashboard";
import AddProvider from "./dashboard/provider/AddProvider";
import ProviderDetails from "./dashboard/provider/ProviderDetails";
import AddProperty from "./dashboard/property/AddProperty";
import PropertyDetails from "./dashboard/property/PropertyDetails";
import PropertyUnits from "./dashboard/property/PropertyUnits";
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
        <Route exact path="/property/add" component={AddProperty} />
        <Route path="/property/:id" component={PropertyDetails} />
        <Route path="/property/:id/units" component={PropertyUnits} />
      </Switch>
    </main>
  );
}

export default Main;
