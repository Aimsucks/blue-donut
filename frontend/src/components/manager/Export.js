import React, { Component } from "react";

import { Row, Col, Button } from "reactstrap";

export class Export extends Component {
    render() {
        return (
            <>
                <Row>
                    <Col>
                        <h2>Export</h2>
                        <p>Temporarily disabled.</p>
                        {/* <Row>
                            <Col md="6">
                                <h4>JSON</h4>
                                <Row>
                                    <Col md="6">
                                        <Button block color="secondary">
                                            Copy
                                        </Button>
                                    </Col>
                                    <Col md="6">
                                        <Button block color="secondary">
                                            Raw
                                        </Button>
                                    </Col>
                                </Row>
                            </Col>
                            <Col md="6">
                                <h4>Wiki</h4>
                                <Row>
                                    <Col md="6">
                                        <Button block color="secondary">
                                            Copy
                                        </Button>
                                    </Col>
                                    <Col md="6">
                                        <Button block color="secondary">
                                            Raw
                                        </Button>
                                    </Col>
                                </Row>
                            </Col>
                        </Row> */}
                    </Col>
                </Row>
            </>
        );
    }
}

export default Export;
