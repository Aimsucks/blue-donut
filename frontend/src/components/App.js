import React, { Component } from "react";
import ReactDOM from "react-dom";
import { HashRouter as Router, Route, Switch } from "react-router-dom";

import { Provider } from "react-redux";
import store from "../store";

import { Provider as AlertProvider } from "react-alert";
import AlertTemplate from "react-alert-template-basic";

import Header from "./layout/Header";
import Footer from "./layout/Footer";

import Alerts from "./layout/Alerts";

import Home from "./home/Home";
import Login from "./login/Login";
import Planner from "./planner/Planner";
import Error from "./error/Error";

// Alert options
const alertOptions = {
    timeout: 3000,
    position: "top center",
    offset: "60px"
};

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <AlertProvider template={AlertTemplate} {...alertOptions}>
                    <Router>
                        <>
                            <Header />
                            <Alerts />
                            <Switch>
                                <Route exact path="/" component={Home} />
                                <Route exact path="/login" component={Login} />
                                <Route
                                    exact
                                    path="/planner"
                                    component={Planner}
                                />
                                <Route component={Error} />
                            </Switch>
                            <div className="extra-space"></div>
                            <Footer />
                        </>
                    </Router>
                </AlertProvider>
            </Provider>
        );
    }
}

ReactDOM.render(<App />, document.getElementById("app"));
