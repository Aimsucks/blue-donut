import React, { Component } from "react";

import { Container } from "reactstrap";

import Splash from "./Splash";
import Tools from "./Tools";

export class Home extends Component {
    render() {
        return (
            <>
                <Splash />
                <Container className="pt-5">
                    <Tools />
                </Container>
            </>
        );
    }
}

export default Home;
