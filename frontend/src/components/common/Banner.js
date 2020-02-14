import React, { Component } from "react";

import { Container, Row, Col } from "reactstrap";

export class Banner extends Component {
    render() {
        return (
            <>
                <Container fluid>
                    <Row className="bg-primary pt-2 pb-4">
                        <Col className="text-center">
                            <h1 className="display-3 mb-0">
                                {this.props.name}
                            </h1>
                        </Col>
                    </Row>
                </Container>
            </>
        );
    }
}

export default Banner;
