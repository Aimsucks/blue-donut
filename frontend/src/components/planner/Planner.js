import React, { Component } from "react";

import { Row, Col } from "reactstrap";

import Destinations from "./Destinations";
import Create from "./Create";

export class Planner extends Component {
    render() {
        return (
            <>
                <Row>
                    <Col className="col-6">
                        <Destinations />
                    </Col>
                    <Col className="col-6">
                        <Create />
                    </Col>
                </Row>
            </>
        );
    }
}

export default Planner;
