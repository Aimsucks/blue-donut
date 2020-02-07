import React, { Component } from "react";

import { Container, Row, Col } from "reactstrap";

export class Banner extends Component {
    render() {
        return (
            <>
                <Container fluid>
                    <Row className="bg-primary py-5">
                        <Col className="text-center">
                            <h1 className="display-3 mb-0">Route Planner</h1>
                        </Col>
                    </Row>
                </Container>
            </>
        );
    }
}

export default Banner;
