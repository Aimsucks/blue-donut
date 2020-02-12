import React, { Component } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getSystems } from "../../actions/map";

import { Row, Col, Input, Button } from "reactstrap";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPen } from "@fortawesome/free-solid-svg-icons";

import { Destination } from "./create/Destination";
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
                <Row className="px-2">
                    <Col md="6" className="px-1">
                        <Destination systems={this.props.systems} />
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
                </Row>
                <Row className="px-2 pt-2">
                    <Col md="12" className="px-1">
                        <Avoid systems={this.props.systems} />
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
            </>
        );
    }
}

export default Create;
