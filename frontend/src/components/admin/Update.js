import React, { Component } from "react";

import { Row, Col, Input, Button } from "reactstrap";

export class Update extends Component {
    render() {
        return (
            <>
                <Row>
                    <Col>
                        <h2>Update Gates</h2>
                        <Row className="justify-content-center">
                            <Col md="8">
                                <Input
                                    type="textarea"
                                    name="gates"
                                    id="gates"
                                />
                                <Button block color="primary" className="mt-3">
                                    Submit
                                </Button>
                            </Col>
                        </Row>
                    </Col>
                </Row>
            </>
        );
    }
}

export default Update;
