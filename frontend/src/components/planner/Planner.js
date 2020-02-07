import React, { Component } from "react";

import { Container, Row, Col } from "reactstrap";

import Banner from "./Banner";
import Destinations from "./Destinations";
import Create from "./Create";

export class Planner extends Component {
    render() {
        return (
            <>
                <Banner />
                <Container className="pt-5">
                    <Row>
                        <Col md="6">
                            <Destinations />
                        </Col>
                        <Col md="6">
                            <Create />
                        </Col>
                    </Row>
                </Container>
            </>
        );
    }
}

export default Planner;
