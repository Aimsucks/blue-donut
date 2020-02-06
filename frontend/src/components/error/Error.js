import React, { Component } from "react";

import { Container, Row, Col } from "reactstrap";

import Header from "../layout/Header";
import Footer from "../layout/Footer";

import Banner from "./Banner";

export class Error extends Component {
    render() {
        return (
            <>
                <Header />
                <Banner />
                <Container className="pt-5">
                    <Row>
                        <Col className="col-6">
                            <h1>
                                These are not the ships you are looking for.
                            </h1>
                        </Col>
                    </Row>
                </Container>
                <Footer />
            </>
        );
    }
}

export default Error;
