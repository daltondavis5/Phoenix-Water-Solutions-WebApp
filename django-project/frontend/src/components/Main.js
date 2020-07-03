import React from "react";
import { Switch, Route } from "react-router-dom";
import Dashboard from "./dashboard/Dashboard";
import AddProvider from "./dashboard/provider/AddProvider";
import ProviderDetails from "./dashboard/provider/ProviderDetails";
import AddProperty from "./dashboard/property/AddProperty";
import PropertyDetails from "./dashboard/property/PropertyDetails";
import PropertyUnits from "./dashboard/property/PropertyUnits";
import Login from "./accounts/login";
import UnitDetails from "./dashboard/units/UnitDetails";

import PrivateRoute from "./common/PrivateRoute";
import MeterDetails from "./dashboard/meter/MeterDetails";

function Main() {
  return (
    <main>
      <Switch>
        <PrivateRoute exact path="/" component={Dashboard} />
        <Route exact path="/login" component={Login} />
        <PrivateRoute exact path="/provider/add" component={AddProvider} />
        <PrivateRoute exact path="/provider/:id" component={ProviderDetails} />
        <PrivateRoute exact path="/property/add" component={AddProperty} />
        <PrivateRoute path="/property/:id" component={PropertyDetails} />
        <PrivateRoute path="/property/:id/units" component={PropertyUnits} />
        <PrivateRoute path="/unit/:id" component={UnitDetails} />
        <PrivateRoute exact path="/meter/:id" component={MeterDetails} />
      </Switch>
    </main>
  );
}

export default Main;
