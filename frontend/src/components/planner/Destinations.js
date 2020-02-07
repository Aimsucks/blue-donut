import React, { Component } from "react";

import { Row, Col } from "reactstrap";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBookmark } from "@fortawesome/free-solid-svg-icons";

import Popular from "./destinations/Popular";
import Favorites from "./destinations/Favorites";
import Recents from "./destinations/Recents";

export class Destinations extends Component {
    render() {
        return (
            <>
                <h2 className="text-center">
                    <FontAwesomeIcon
                        icon={faBookmark}
                        size="sm"
                        className="mr-2 pb-1"
                    />
                    Destinations
                </h2>
                <Row>
                    <Col md="4">
                        <Popular />
                    </Col>
                    <Col md="4">
                        <Favorites />
                    </Col>
                    <Col cmd="4">
                        <Recents />
                    </Col>
                </Row>
            </>
        );
    }
}

export default Destinations;
