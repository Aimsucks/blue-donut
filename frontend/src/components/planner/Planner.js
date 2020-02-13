import React, { Component } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getSystems } from "../../actions/map";

import { Container, Row, Col } from "reactstrap";

import Banner from "./Banner";
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
    }

    render() {
        return (
            <>
                <Banner />
                <Container className="pt-5">
                    <Row>
                        <Col md="6">
                            <Destinations systems={this.props.systems} />
                        </Col>
                        <Col md="6">
                            <Create systems={this.props.systems} />
                        </Col>
                    </Row>
                    {this.props.route.length ? (
                        <Row className="justify-content-center mt-2">
                            <Col md="6">
                                <Map route={this.props.route} />
                            </Col>
                            <Col md="2">
                                <Trip route={this.props.route} />
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
