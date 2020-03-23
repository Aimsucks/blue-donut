import React, { Component } from "react";

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

export class Feedback extends Component {
    render() {
        return (
            <>
                <Modal isOpen={this.state.modal} toggle={this.toggle}>
                    <ModalHeader toggle={this.toggle}>Feedback</ModalHeader>
                    <ModalBody>
                        <p>Hello!</p>
                    </ModalBody>
                    <ModalFooter>
                        <Button color="primary">Submit</Button>
                        <Button color="secondary">Cancel</Button>
                    </ModalFooter>
                </Modal>
            </>
        );
    }
}

export default Feedback;
