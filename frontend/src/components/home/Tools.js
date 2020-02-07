import React, { Component } from "react";

import { Row, Col, Button } from "reactstrap";

import { Link } from "react-router-dom";

export class Options extends Component {
    render() {
        return (
            <>
                <Row>
                    <Col md="4" className="text-center">
                        <h2>Route Planner</h2>
                        <p className="lead">
                            Navigate via our jump bridge network
                        </p>
                        <Link to="/planner">
                            <Button color="primary" className="btn-lg">
                                Set destination
                            </Button>
                        </Link>
                    </Col>
                    <Col md="4" className="text-center">
                        <h2>Scans</h2>
                        <p className="lead">
                            Submit a local or directional scan
                        </p>
                        <Link to="/scanner">
                            <Button
                                color="secondary"
                                className="btn-lg"
                                disabled
                            >
                                Work in progress
                            </Button>
                        </Link>
                    </Col>
                    <Col md="4" className="text-center">
                        <h2>Appraisal</h2>
                        <p className="lead">
                            Instantly appraise your inventory
                        </p>
                        <Link to="/appraisal">
                            <Button
                                href=""
                                color="secondary"
                                className="btn-lg"
                                disabled
                            >
                                Work in progress
                            </Button>
                        </Link>
                    </Col>
                </Row>
            </>
        );
    }
}

export default Options;
