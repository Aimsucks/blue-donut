import React, { Component } from "react";
import { connect } from "react-redux";
import { hideFeedback, sendFeedback } from "../../actions/feedback";

import {
    Modal,
    ModalHeader,
    ModalBody,
    Form,
    Row,
    Col,
    FormGroup,
    CustomInput,
    Label,
    Input,
    ModalFooter,
    Button
} from "reactstrap";

export class Feedback extends Component {
    constructor(props) {
        super(props);
        this.state = {
            experience: "good",
            feedback: ""
        };
    }

    onChange(key, event) {
        this.setState({
            [key]: event.target.value
        });
    }

    onFormSubmit() {
        this.props.sendFeedback({
            experience: this.state.experience,
            feedback: this.state.feedback,
            characterID: localStorage.getItem("activeCharacter")
        });
        this.props.hideFeedback();
        this.setState({
            experience: "good",
            feedback: ""
        });
    }

    render() {
        return (
            <>
                <Modal isOpen={this.props.show}>
                    <ModalHeader>Feedback</ModalHeader>
                    <ModalBody>
                        <Form>
                            <Row form>
                                <Col md="12">
                                    <FormGroup>
                                        <Label for="experience">
                                            How was your experience?
                                        </Label>
                                        <CustomInput
                                            type="radio"
                                            id="bad"
                                            label="Bad"
                                            name="experienceRadio"
                                            checked={
                                                this.state.experience === "bad"
                                            }
                                            onChange={this.onChange.bind(
                                                this,
                                                "experience"
                                            )}
                                            value="bad"
                                        />
                                        <CustomInput
                                            type="radio"
                                            id="good"
                                            label="Good"
                                            name="experienceRadio"
                                            checked={
                                                this.state.experience === "good"
                                            }
                                            onChange={this.onChange.bind(
                                                this,
                                                "experience"
                                            )}
                                            value="good"
                                        />
                                    </FormGroup>
                                </Col>
                            </Row>
                            <Row form>
                                <Col md="12">
                                    <FormGroup>
                                        <Label for="experience">Feedback</Label>
                                        <Input
                                            type="textarea"
                                            maxLength="2000"
                                            rows="4"
                                            value={this.state.feedback}
                                            onChange={this.onChange.bind(
                                                this,
                                                "feedback"
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
                        <Button
                            color="secondary"
                            onClick={this.props.hideFeedback}
                        >
                            Cancel
                        </Button>
                    </ModalFooter>
                </Modal>
            </>
        );
    }
}

const mapStateToProps = state => ({
    show: state.feedback.show
});

export default connect(mapStateToProps, { hideFeedback, sendFeedback })(
    Feedback
);
