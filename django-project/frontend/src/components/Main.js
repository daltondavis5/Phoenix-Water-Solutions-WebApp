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
        <Route exact path="/" component={Dashboard} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/provider/add" component={AddProvider} />
        <Route exact path="/provider/:id" component={ProviderDetails} />
        <Route exact path="/property/add" component={AddProperty} />
        <Route path="/property/:id" component={PropertyDetails} />
        <Route path="/property/:id/units" component={PropertyUnits} />
        <Route path="/unit/:id" component={UnitDetails} />
        <Route exact path="/meter/:id" component={MeterDetails} />
      </Switch>
    </main>
  );
}

export default Main;
