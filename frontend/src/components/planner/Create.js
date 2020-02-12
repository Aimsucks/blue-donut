import React, { Component } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getSystems } from "../../actions/map";

import { Row, Col, Form, Input, Button } from "reactstrap";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPen } from "@fortawesome/free-solid-svg-icons";

import { Destination } from "./create/Destination";
import { Origin } from "./create/Origin";
import { Avoid } from "./create/Avoid";

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
                <Form action="/api/route/">
                    <Input
                        name="id"
                        id="characterID"
                        value={localStorage.getItem("activeCharacter")}
                        hidden
                        readOnly
                    />
                    <Row className="px-2">
                        <Col md="6" className="px-1">
                            <Origin systems={this.props.systems} />
                        </Col>
                        <Col md="6" className="px-1">
                            <Destination systems={this.props.systems} />
                        </Col>
                    </Row>
                    <Row className="px-2 pt-2">
                        <Col md="6" className="px-1">
                            <Avoid systems={this.props.systems} />
                        </Col>
                        <Col md="3" className="px-1">
                            <Button href="" block color="primary" type="submit">
                                Verify
                            </Button>
                        </Col>
                        <Col md="3" className="px-1">
                            <Button href="" block color="primary">
                                Generate
                            </Button>
                        </Col>
                    </Row>
                    <Row className="px-2">
                        <Col className="px-1">
                            <small className="mt-1 ml-2">
                                <a href="" className="text-info">
                                    Report an incorrect jump gate.
                                </a>
                            </small>
                        </Col>
                    </Row>
                </Form>
            </>
        );
    }
}

export default Create;
