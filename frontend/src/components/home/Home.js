import React, { Component } from "react";

import { Container } from "reactstrap";

import Header from "../layout/Header";
import Footer from "../layout/Footer";

import Splash from "./Splash";
import Tools from "./Tools";

export class Home extends Component {
    render() {
        return (
            <>
                <Header />
                <Splash />
                <Container className="pt-5">
                    <Tools />
                </Container>
                <Footer />
            </>
        );
    }
}

export default Home;
