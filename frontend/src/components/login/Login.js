import React, { Component } from "react";

import { Container, Row, Col, Form, FormGroup, CustomInput, Button, Collapse, Card, CardBody } from "reactstrap";

import Banner from "./Banner";

export class Error extends Component {
    constructor(props) {
        super(props);
        this.state = {
            collapse: false
        };
        this.toggleCollapse = this.toggleCollapse.bind(this);
    }

    toggleCollapse() {
        this.setState({ collapse: !this.state.collapse })
    }

    render() {
        const show = (this.state.collapse) ? true : false;

        return (
            <>
                <Banner />
                <Container className="pt-5">
                    <Row className="justify-content-center">
                        <Col md="6">
                            <Form action="/auth/login/">
                                <h2 className="text-center">
                                    Scope Selection
                                </h2>
                                <p>
                                    Would you like to give us access to additional
                                    scopes so we can search your alliance's jump
                                    gates and add them to our tool?
                                </p>
                                <FormGroup className="pr-2 text-center">
                                    <CustomInput type="checkbox" id="scopes" name="scopes" label="Search and read structures" />
                                </FormGroup>
                                <div className="text-center">
                                    <Button onClick={this.toggleCollapse} color="secondary">
                                        Additional information
                                    </Button>
                                </div>
                                <Collapse isOpen={show}>
                                    <Card className="mt-3 border-secondary">
                                        <CardBody>
                                            <p className="card-text">
                                                Checking this box means you will give us access to the following scopes:
                                            </p>
                                            <ul>
                                                <li>esi-search.search_structures.v1</li>
                                                <li>esi-universe.read_structures.v1</li>
                                            </ul>
                                            <p>
                                                We use these scopes to search the structures you can see through ESI for the
                                                ">>" character found in all Ansiblex Jump Gate names, as well as a letter following
                                                it because ESI has some weird limitations on how many results it will return.
                                            </p>

                                            <p className="card-text">This process can be seen in {" "}
                                                <a className="text-info" href="https://github.com/Aimsucks/blue_donut/blob/master/jump_bridges/backend.py">this file</a>.
                                            </p>
                                            <p className="card-text">
                                                However, this scope gives us access to read <i>every single one</i> of the structures
                                                you have access to. Because of that, we are giving you the ability to choose whether
                                                you trust us with that kind of power.
                                            </p>
                                            <p className="card-text">
                                                Blue Donut is and always will be 100% open-source. The code running on the website is
                                                available on {" "}
                                                <a className="text-info" href="https://github.com/Aimsucks/blue_donut">GitHub</a>.
                                            </p>
                                        </CardBody>
                                    </Card>
                                </Collapse>
                                <Row className="justify-content-center mt-3">
                                    <Col md="8">
                                        <Button block color="primary">Continue to EVE SSO</Button>
                                    </Col>
                                </Row>
                            </Form>
                        </Col>
                    </Row>
                </Container>
            </>
        );
    }
}

export default Error;
