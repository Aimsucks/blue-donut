import React, { Component } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getSystems } from "../../actions/map";

import { Container, Row, Col } from "reactstrap";

import Banner from "./Banner";
import Destinations from "./Destinations";
import Create from "./Create";

export class Planner extends Component {
    static propTypes = {
        systems: PropTypes.array
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
                </Container>
            </>
        );
    }
}

const mapStateToProps = state => ({
    systems: state.map.systems
});

export default connect(mapStateToProps, { getSystems })(Planner);
