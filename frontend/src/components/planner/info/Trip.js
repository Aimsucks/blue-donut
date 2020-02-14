import React, { Component } from "react";

import { connect } from "react-redux";
import { sendRoute } from "../../../actions/route";

import { CopyToClipboard } from "react-copy-to-clipboard";

import { Row, Col, Button } from "reactstrap";

export class Trip extends Component {
    handleButtonClick = e => {
        e.preventDefault();
        this.props.sendRoute({
            path: this.props.route.network_path,
            character: localStorage.getItem("activeCharacter")
        });
    };
    render() {
        console.log(this.props.route);
        return (
            <>
                <Row className="pt-2 px-2">
                    <Col md="6" className="px-1">
                        <h1 className="text-center mb-0">
                            {this.props.route.destination}
                        </h1>
                        <p class="mb-2 text-muted text-center">
                            {this.props.route.length} jumps
                        </p>
                    </Col>
                    <Col md="6" className="px-1 my-auto">
                        {this.props.route.confirm_button ? (
                            <Button
                                block
                                color="primary"
                                onClick={this.handleButtonClick}
                            >
                                Set destination
                            </Button>
                        ) : null}
                        <CopyToClipboard
                            text={
                                this.props.route.origin
                                    ? "https://bluedonut.space/planner?to=" +
                                      this.props.route.destination +
                                      "&from=" +
                                      this.props.route.origin
                                    : "https://bluedonut.space/planner?to=" +
                                      this.props.route.destination
                            }
                        >
                            <Button block color="secondary">
                                Copy sharable link
                            </Button>
                        </CopyToClipboard>
                    </Col>
                </Row>
            </>
        );
    }
}

export default connect(null, { sendRoute })(Trip);
