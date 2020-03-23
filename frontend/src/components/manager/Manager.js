import React, { Component } from "react";

import { Container, Row, Col } from "reactstrap";

import Banner from "../common/Banner";
import Statistics from "./Statistics";
import Export from "./Export";
import Update from "./Update";

export class Admin extends Component {
    render() {
        return (
            <>
                <Banner name="Manager" />
                <Container className="pt-5">
                    <Row className="justify-content-center">
                        <Col md="6" className="text-center">
                            <Statistics />
                            <hr />
                            <Export />
                            <hr />
                            <Update />
                        </Col>
                    </Row>
                </Container>
            </>
        );
    }
}

export default Admin;
