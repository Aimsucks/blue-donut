import React, { Component } from "react";

import { Row, Col, Input, Button } from "reactstrap";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPen } from "@fortawesome/free-solid-svg-icons";

export class Create extends Component {
    render() {
        return (
            <>
                <h2 className="text-center">
                    <FontAwesomeIcon
                        icon={faPen}
                        size="sm"
                        className="mr-2 pb-1"
                    />
                    Create Your Own
                </h2>
                <Row className="px-2">
                    <Col md="6" className="px-1">
                        <Input name="system" placeholder="Destination" />
                    </Col>
                    <Col md="3" className="px-1">
                        <Button href="" className="btn-block" color="primary">
                            Verify
                        </Button>
                    </Col>
                    <Col md="3" className="px-1">
                        <Button href="" className="btn-block" color="primary">
                            Generate
                        </Button>
                    </Col>
                    <small className="mt-1 ml-2">
                        <a href="" className="text-info">
                            Report an incorrect jump gate.
                        </a>
                    </small>
                </Row>
            </>
        );
    }
}

export default Create;
