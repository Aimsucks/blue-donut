import React, { Component } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getStatistics } from "../../actions/manager";

import { Row, Col, Table } from "reactstrap";

export class Statistics extends Component {
    static propTypes = {
        statistics: PropTypes.object.isRequired
    };

    componentDidMount() {
        this.props.getStatistics();
    }

    render() {
        return (
            <>
                {Object.keys(this.props.statistics).length && (
                    <Row>
                        <Col>
                            <h2>Statistics</h2>
                            <Row>
                                <Col md="4">
                                    <h4>Users</h4>
                                    <Table bordered>
                                        <tbody>
                                            {this.props.statistics.users.map(
                                                (value, index) => {
                                                    return (
                                                        <tr key={index}>
                                                            <td>
                                                                {value.name}
                                                            </td>
                                                            <td>
                                                                {value.number}
                                                            </td>
                                                        </tr>
                                                    );
                                                }
                                            )}
                                        </tbody>
                                    </Table>
                                </Col>
                                <Col md="4">
                                    <h4>Map</h4>
                                    <Table bordered>
                                        <tbody>
                                            {this.props.statistics.map.map(
                                                (value, index) => {
                                                    return (
                                                        <tr key={index}>
                                                            <td>
                                                                {value.name}
                                                            </td>
                                                            <td>
                                                                {value.number}
                                                            </td>
                                                        </tr>
                                                    );
                                                }
                                            )}
                                        </tbody>
                                    </Table>
                                </Col>
                                <Col md="4">
                                    <h4>Planner</h4>
                                    <Table bordered>
                                        <tbody>
                                            {this.props.statistics.bridges.map(
                                                (value, index) => {
                                                    return (
                                                        <tr key={index}>
                                                            <td>
                                                                {value.name}
                                                            </td>
                                                            <td>
                                                                {value.number}
                                                            </td>
                                                        </tr>
                                                    );
                                                }
                                            )}
                                        </tbody>
                                    </Table>
                                </Col>
                            </Row>
                        </Col>
                    </Row>
                )}
            </>
        );
    }
}

const mapStateToProps = state => ({
    statistics: state.statistics.statistics
});

export default connect(mapStateToProps, { getStatistics })(Statistics);
