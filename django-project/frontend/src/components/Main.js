import React from "react";
import { Switch, Route } from "react-router-dom";
import Dashboard from "./dashboard/Dashboard";
import AddProvider from "./dashboard/provider/AddProvider";
import EditProvider from "./dashboard/provider/EditProvider";
import ProviderDetails from "./dashboard/provider/ProviderDetails";

function Main() {
  return (
    <main>
      <Switch>
        <Route exact path="/" component={Dashboard} />
        <Route exact path="/provider/add" component={AddProvider} />
        <Route exact path="/provider/edit/:id" component={EditProvider} />
        <Route exact path="/provider/:id" component={ProviderDetails} />
      </Switch>
    </main>
  );
}

export default Main;
