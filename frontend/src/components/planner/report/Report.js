import React, { Component, useState } from "react";

import { connect } from "react-redux";
import { sendReport } from "../../../actions/report";

import {
    Modal,
    ModalHeader,
    ModalBody,
    Form,
    Row,
    Col,
    FormGroup,
    Label,
    Input,
    ModalFooter,
    Button
} from "reactstrap";

import { OutageType } from "./OutageType";
import { SystemPicker } from "./SystemPicker";
import { faThList } from "@fortawesome/free-solid-svg-icons";

export class Report extends Component {
    constructor(props) {
        super(props);
        this.state = {
            modal: false,
            outageType: "offline",
            incorrectFrom: null,
            incorrectTo: null,
            correctFrom: null,
            correctTo: null,
            extraInformation: "",
            characterID: ""
        };

        this.toggle = this.toggle.bind(this);
        this.onSelectChange = this.onSelectChange.bind(this);
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
            });
        }
        this.setState({
            modal: !this.state.modal
        });
    }

    onValueChange(key, event) {
        this.setState({ [key]: event.target.value });
    }

    onSelectChange = name => value => {
        this.setState({ [name]: value });
    };

    onFormSubmit() {
        this.setState({
            characterID: localStorage.getItem("activeCharacter")
        });
        if (this.state.characterID) {
            this.props.sendReport({
                outageType: this.state.outageType,
                incorrectFrom: this.state.incorrectFrom.value,
                incorrectTo: this.state.incorrectTo.value,
                correctFrom: this.state.correctFrom.value,
                correctTo: this.state.correctTo.value,
                extraInformation: this.state.extraInformation,
                characterID: this.state.characterID
            });
        }
        this.toggle();
    }

    render() {
        return (
            <>
                <small>
                    <a
                        className="text-info clickable-link"
                        onClick={this.toggle}
                    >
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
                                        <OutageType
                                            value={this.state.outageType}
                                            onValueChange={this.onValueChange.bind(
                                                this,
                                                "outageType"
                                            )}
                                        />
                                    </FormGroup>
                                </Col>
                            </Row>
                            {[
                                "offline",
                                "fuel",
                                "incorrect",
                                "loopback",
                                "missingTool"
                            ].includes(this.state.outageType) ? (
                                <SystemPicker
                                    incorrect
                                    name="incorrect"
                                    from={this.state.incorrectFrom}
                                    onSelectChangeFrom={this.onSelectChange(
                                        "incorrectFrom"
                                    )}
                                    to={this.state.incorrectTo}
                                    onSelectChangeTo={this.onSelectChange(
                                        "incorrectTo"
                                    )}
                                />
                            ) : null}
                            {["incorrect", "missingIngame"].includes(
                                this.state.outageType
                            ) ? (
                                <SystemPicker
                                    name="correct"
                                    from={this.state.correctFrom}
                                    handleFrom={this.onSelectChange.bind(
                                        this,
                                        "correctFrom"
                                    )}
                                    to={this.state.correctTo}
                                    handleTo={this.onSelectChange.bind(
                                        this,
                                        "correctTo"
                                    )}
                                />
                            ) : null}
                            <Row form>
                                <Col md="12">
                                    <FormGroup>
                                        <Label for="extraInformation">
                                            Extra Information
                                        </Label>
                                        <Input
                                            type="textarea"
                                            name="extraInformation"
                                            id="extraInformation"
                                            value={this.state.extraInformation}
                                            onChange={this.onValueChange.bind(
                                                this,
                                                "extraInformation"
                                            )}
                                        />
                                    </FormGroup>
                                </Col>
                            </Row>
                        </Form>
                    </ModalBody>
                    <ModalFooter>
                        <Button
                            color="primary"
                            onClick={() => this.onFormSubmit()}
                        >
                            Submit
                        </Button>
                        <Button color="secondary" onClick={this.toggle}>
                            Cancel
                        </Button>
                    </ModalFooter>
                </Modal>
            </>
        );
    }
}

export default connect(null, { sendReport })(Report);
