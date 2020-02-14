import React, { Component } from "react";
import { Redirect } from "react-router-dom";
import queryString from "query-string";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getSystems } from "../../actions/map";

import { Container, Row, Col } from "reactstrap";

import Banner from "../common/Banner";
import Destinations from "./destinations/Destinations";
import Create from "./create/Create";
import Map from "./info/Map";
import Trip from "./info/Trip";

export class Planner extends Component {
    static propTypes = {
        systems: PropTypes.array,
        route: PropTypes.object
    };

    componentDidMount() {
        this.props.getSystems();
        const values = queryString.parse(this.props.location.search);
        this.props.route.to = { value: values.to, label: values.to };
        this.props.route.from = { value: values.from, label: values.from };
    }

    render() {
        return (
            <>
                <Banner name="Route Planner" />
                <Container className="pt-5">
                    <Row>
                        <Col md="6">
                            <Destinations systems={this.props.systems} />
                        </Col>
                        <Col md="6">
                            <Create systems={this.props.systems} />
                            {this.props.route.length ? (
                                <Trip route={this.props.route} />
                            ) : null}
                        </Col>
                    </Row>
                    {this.props.route.length ? (
                        <Row className="justify-content-center mt-2">
                            <Col>
                                <Map route={this.props.route} />
                            </Col>
                        </Row>
                    ) : null}
                </Container>
            </>
        );
    }
}

const mapStateToProps = state => ({
    systems: state.map.systems,
    route: state.route.route
});

export default connect(mapStateToProps, { getSystems })(Planner);
