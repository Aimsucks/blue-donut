import React, { Component } from "react";
import ReactDOM from "react-dom";
import { HashRouter as Router, Route, Switch, Redirect } from "react-router-dom";

import { Provider } from "react-redux";
import store from "../store";

import Header from "./layout/Header"
import Footer from "./layout/Footer"

import Home from "./home/Home";
import Planner from "./planner/Planner";
import Error from "./error/Error";

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <Router>
                    <>
                        <Header />
                        <Switch>
                            <Route exact path="/" component={Home} />
                            <Route exact path="/planner" component={Planner} />
                            <Route component={Error} />
                        </Switch>
                        <Footer />
                    </>
                </Router>
            </Provider>
        );
    }
}

ReactDOM.render(<App />, document.getElementById("app")
);
