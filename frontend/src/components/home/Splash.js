import React, { Component } from "react";

import { Container, Row, Col } from "reactstrap";

export class Splash extends Component {
    render() {
        const splashStyle = {
            background: "url('/static/img/donut.png')",
            backgroundSize: "750px",
            backgroundRepeat: "no-repeat",
            backgroundPosition: "center 30px"
        };

        return (
            <>
                <Container fluid>
                    <Row className="bg-primary py-5" style={splashStyle}>
                        <Col className="text-center py-5">
                            <h1 className="display-3 mb-0">Blue Donut</h1>
                            <p className="lead">
                                Tools to help you live in the blue donut
                        </p>
                        </Col>
                    </Row>
                </Container>
            </>
        );
    }
}

export default Splash;
