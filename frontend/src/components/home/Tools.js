import React, { Component } from "react";

import { Row, Col, Button } from "reactstrap";

export class Options extends Component {
    render() {
        return (
            <>
                <Row>
                    <Col className="col-4 text-center">
                        <h2>Route Planner</h2>
                        <p className="lead">
                            Navigate via our jump bridge network
                        </p>
                        <Button href="" color="primary" className="btn-lg">
                            Set destination
                        </Button>
                    </Col>
                    <Col className="col-4 text-center">
                        <h2>Scans</h2>
                        <p className="lead">
                            Submit a local or directional scan
                        </p>
                        <Button
                            href=""
                            color="secondary"
                            className="btn-lg"
                            disabled
                        >
                            Work in progress
                        </Button>
                    </Col>
                    <Col className="col-4 text-center">
                        <h2>Appraisal</h2>
                        <p className="lead">
                            Instantly appraise your inventory
                        </p>
                        <Button
                            href=""
                            color="secondary"
                            className="btn-lg"
                            disabled
                        >
                            Work in progress
                        </Button>
                    </Col>
                </Row>
            </>
        );
    }
}

export default Options;
