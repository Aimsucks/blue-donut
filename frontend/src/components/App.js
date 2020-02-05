import React, { Component } from "react";
import ReactDOM from "react-dom";

import { Container } from "reactstrap";

import Header from "./layout/Header";
import Footer from "./layout/Footer";

import Splash from "./home/Splash";
import Tools from "./home/Tools";

import Banner from "./Banner";
import Planner from "./planner/Planner";

class App extends Component {
    render() {
        return (
            <>
                <Header />
                {/* <Splash /> */}
                <Banner />
                <Container className="pt-5">
                    {/* <Tools /> */}
                    <Planner />
                </Container>
                <Footer />
            </>
        );
    }
}

ReactDOM.render(<App />, document.getElementById("app"));
