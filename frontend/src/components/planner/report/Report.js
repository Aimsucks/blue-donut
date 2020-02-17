import React, { Component, useState } from 'react'

import { connect } from "react-redux";
import { sendReport } from "../../../actions/report";

import { Modal, ModalHeader, ModalBody, Form, Row, Col, FormGroup, Label, Input, ModalFooter, Button } from 'reactstrap'

import { OutageType } from './OutageType'
import { SystemPicker } from './SystemPicker'

export class Report extends Component {
    constructor(props) {
        super(props);
        this.state = {
            modal: false,
            outageType: "offline",
            incorrectFrom: "",
            incorrectTo: "",
            correctFrom: "",
            correctTo: "",
            extraInformation: "",
            characterID: ""
        };

        this.toggle = this.toggle.bind(this)
    }

    toggle() {
        if (this.state.modal) {
            this.setState({
                outageType: "offline",
                incorrectFrom: "",
                incorrectTo: "",
                correctFrom: "",
                correctTo: "",
                extraInformation: ""
            })
        }
        this.setState({
            modal: !this.state.modal
        });
    }

    onValueChange(key, event) {
        this.setState({ [key]: event.target.value })
    }

    onFormSubmit() {
        this.setState({
            characterID: localStorage.getItem("activeCharacter")
        })
        if (this.state.characterID) {
            this.props.sendReport(this.state)
        }
        this.toggle()
    }

    onSubmit = e => {
        e.preventDefault();
        let character = localStorage.getItem("activeCharacter");
        let { from, to, avoid, confirm } = this.state;
        if (avoid) avoid = avoid.map(a => a.value);
        if (from) from = from.value;
        to = to ? to.value : null;
        const plan = { character, from, to, avoid, confirm };
        this.props.getRoute(plan)
        if (confirm && to) {
            this.props.sendRecents({ to: to })
        }
        this.setState({ confirm: false });
    }

    render() {
        return (
            <>
                <small>
                    <a className="text-info clickable-link" onClick={this.toggle}>
                        Report an incorrect jump gate.
                    </a>
                </small>
                <Modal isOpen={this.state.modal} toggle={this.toggle}>
                    <ModalHeader toggle={this.toggle}>
                        Outage Report
                    </ModalHeader>
                    <ModalBody>
                        <Form className="text-center">
                            <Row form>
                                <Col md="12">
                                    <FormGroup>
                                        <OutageType value={this.state.outageType} onValueChange={this.onValueChange.bind(this, 'outageType')} />
                                    </FormGroup>
                                </Col>
                            </Row>
                            {["offline", "fuel", "incorrect", "loopback", "missingTool"].includes(this.state.outageType) ?
                                <SystemPicker
                                    incorrect
                                    name="incorrect"
                                    from={this.state.incorrectFrom}
                                    handleFrom={this.onValueChange.bind(this, 'incorrectFrom')}
                                    to={this.state.incorrectTo}
                                    handleTo={this.onValueChange.bind(this, 'incorrectTo')} />
                                : null}
                            {["incorrect", "missingIngame"].includes(this.state.outageType) ?
                                <SystemPicker
                                    name="correct"
                                    from={this.state.correctFrom}
                                    handleFrom={this.onValueChange.bind(this, 'correctFrom')}
                                    to={this.state.correctTo}
                                    handleTo={this.onValueChange.bind(this, 'correctTo')} />
                                : null}
                            <Row form>
                                <Col md="12">
                                    <FormGroup>
                                        <Label for="extraInformation">Extra Information</Label>
                                        <Input
                                            type="textarea"
                                            name="extraInformation"
                                            id="extraInformation"
                                            value={this.state.extraInformation}
                                            onChange={this.onValueChange.bind(this, 'extraInformation')} />
                                    </FormGroup>
                                </Col>
                            </Row>
                        </Form>
                    </ModalBody>
                    <ModalFooter>
                        <Button color="primary" onClick={() => this.onFormSubmit()}>Submit</Button>
                        <Button color="secondary" onClick={this.toggle}>Cancel</Button>
                    </ModalFooter>
                </Modal>
            </>
        )
    }
}

export default connect(null, { sendReport })(Report)
