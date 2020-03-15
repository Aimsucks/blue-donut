import React, { Component } from "react";

import { Row, Col, FormGroup, Label, Input } from "reactstrap";

import SystemSelect from "../../common/SystemSelect";

export class SystemPicker extends Component {
    render() {
        return (
            <>
                <Row form>
                    <Col md="12">
                        <h4>
                            {this.props.incorrect
                                ? "Planned Connection"
                                : "Corrected Connection"}
                        </h4>
                        <p className="text-muted mb-1">
                            '
                            {this.props.incorrect
                                ? "The jump gate connection the route planner wants you to take."
                                : "The jump gate connection that is missing from the route planner."}
                        </p>
                    </Col>
                </Row>
                <Row form>
                    <Col md="6">
                        <FormGroup>
                            <Label for={this.props.name + "FromSystem"}>
                                From
                            </Label>
                            <SystemSelect
                                name={this.props.name + "FromSystem"}
                                value={this.props.from}
                                onSelectChange={this.props.onSelectChangeFrom}
                                placeholder="System"
                            />
                        </FormGroup>
                    </Col>
                    <Col md="6">
                        <FormGroup>
                            <Label for={this.props.name + "ToSystem"}>To</Label>
                            <SystemSelect
                                name={this.props.name + "ToSystem"}
                                value={this.props.to}
                                onSelectChange={this.props.onSelectChangeTo}
                                placeholder="System"
                            />
                        </FormGroup>
                    </Col>
                </Row>
            </>
        );
    }
}

export default SystemPicker;
