import React, { Component } from 'react'

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getSystems } from "../../../actions/map"

import { Row, Col, FormGroup, Label, Input } from 'reactstrap'

export class SystemPicker extends Component {
    static propTypes = {
        systems: PropTypes.array
    };

    render() {
        console.log(this.props.systems)
        return (
            <>
                <Row form>
                    <Col md="12">
                        <h4>{this.props.incorrect ? "Planned Connection" : "Corrected Connection"}</h4>
                        <p className="text-muted mb-1">'
                            {this.props.incorrect ?
                                "The jump gate connection the route planner wants you to take."
                                : "The jump gate connection that is missing from the route planner."}
                        </p>
                    </Col>
                </Row>
                <Row form>
                    <Col md="6">
                        <FormGroup>
                            <Label for={this.props.name + "FromSystem"}>From</Label>
                            <Input
                                type="text"
                                name={this.props.name + "From"}
                                id={this.props.name + "FromSystem"}
                                placeholder="System name"
                                value={this.props.from}
                                onChange={this.props.handleFrom} />
                        </FormGroup>
                    </Col>
                    <Col md="6">
                        <FormGroup>
                            <Label for={this.props.name + "ToSystem"}>To</Label>
                            <Input
                                type="text"
                                name={this.props.name + "To"}
                                id={this.props.name + "ToSystem"}
                                placeholder="System name"
                                value={this.props.to}
                                onChange={this.props.handleTo} />
                        </FormGroup>
                    </Col>
                </Row>
            </>
        )
    }
}

const mapStateToProps = state => {
    console.log(state)
    return {
        systems: state.map.systems
    }
};

export default connect(mapStateToProps)(SystemPicker);
