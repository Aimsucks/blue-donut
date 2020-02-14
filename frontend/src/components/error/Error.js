import React, { Component } from "react";

import { Container, Row, Col } from "reactstrap";

import Banner from "../common/Banner";

export class Error extends Component {
    render() {
        return (
            <>
                <Banner name="Error" />
                <Container className="pt-5">
                    <Row className="justify-content-center">
                        <Col md="6" className="col-6">
                            <h1>
                                These are not the ships you are looking for.
                            </h1>
                        </Col>
                    </Row>
                </Container>
            </>
        );
    }
}

export default Error;
