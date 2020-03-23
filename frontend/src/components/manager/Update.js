import React, { Component } from "react";

import { connect } from "react-redux";
import { sendBridges } from "../../actions/manager";

import { Row, Col, Input, Button } from "reactstrap";

export class Update extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: ""
        };
    }

    onChange(event) {
        this.setState({
            data: event.target.value
        });
    }

    onFormSubmit() {
        this.props.sendBridges({
            data: this.state.data,
            characterID: localStorage.getItem("activeCharacter")
        });
    }

    render() {
        return (
            <>
                <Row>
                    <Col>
                        <h2>Update Gates</h2>
                        <Row className="justify-content-center">
                            <Col md="8">
                                <Input
                                    type="textarea"
                                    name="gates"
                                    id="gates"
                                    value={this.state.data}
                                    onChange={event => this.onChange(event)}
                                />
                                <Button
                                    onClick={() => this.onFormSubmit()}
                                    block
                                    color="primary"
                                    className="mt-3"
                                >
                                    Submit
                                </Button>
                            </Col>
                        </Row>
                    </Col>
                </Row>
            </>
        );
    }
}

export default connect(null, { sendBridges })(Update);
