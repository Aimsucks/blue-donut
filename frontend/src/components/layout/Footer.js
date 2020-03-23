import React, { useState } from "react";

import { connect } from "react-redux";
import { showFeedback } from "../../actions/feedback";

import {
    Navbar,
    Container,
    Nav,
    NavItem,
    NavLink,
    UncontrolledTooltip
} from "reactstrap";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGithub, faDiscord } from "@fortawesome/free-brands-svg-icons";
import { faMugHot, faCommentDots } from "@fortawesome/free-solid-svg-icons";

export class Footer extends React.Component {
    render() {
        return (
            <>
                <div className="footer fixed-bottom">
                    <Navbar dark>
                        <Container>
                            <Nav navbar className="mr-auto">
                                <NavItem className="text-muted">
                                    Made by{" "}
                                    <a
                                        className="text-info"
                                        href="https://evewho.com/character/2113697818"
                                    >
                                        Aimsucks{" "}
                                    </a>
                                    with help from{" "}
                                    <a
                                        className="text-info"
                                        href="https://evewho.com/character/94944046"
                                    >
                                        Callum Lul{" "}
                                    </a>
                                    and{" "}
                                    <a
                                        className="text-info"
                                        href="https://evewho.com/character/94854191"
                                    >
                                        Telltak Laellithor
                                    </a>
                                </NavItem>
                            </Nav>
                            <Nav navbar className="ml-auto navbar-expand-md">
                                <NavItem>
                                    <NavLink
                                        className="px-2"
                                        onClick={this.props.showFeedback}
                                        href="#"
                                        id="feedback"
                                    >
                                        <FontAwesomeIcon
                                            icon={faCommentDots}
                                            size="2x"
                                        />
                                    </NavLink>
                                    <UncontrolledTooltip
                                        placement="top"
                                        target={"feedback"}
                                    >
                                        Feedback
                                    </UncontrolledTooltip>
                                </NavItem>
                                <NavItem>
                                    <NavLink
                                        className="px-2"
                                        href="https://ko-fi.com/aimsucks"
                                        target="_blank"
                                        id="donate"
                                    >
                                        <FontAwesomeIcon
                                            icon={faMugHot}
                                            size="2x"
                                        />
                                    </NavLink>
                                    <UncontrolledTooltip
                                        placement="top"
                                        target={"donate"}
                                    >
                                        Donate
                                    </UncontrolledTooltip>
                                </NavItem>
                                <NavItem>
                                    <NavLink
                                        className="px-2"
                                        href="https://github.com/Aimsucks/blue-donut"
                                        target="_blank"
                                        id="github"
                                    >
                                        <FontAwesomeIcon
                                            icon={faGithub}
                                            size="2x"
                                        />
                                    </NavLink>
                                    <UncontrolledTooltip
                                        placement="top"
                                        target={"github"}
                                    >
                                        GitHub
                                    </UncontrolledTooltip>
                                </NavItem>
                                <NavItem>
                                    <NavLink
                                        className="px-2"
                                        href="https://discord.gg/UCK8ase"
                                        target="_blank"
                                        id="discord"
                                    >
                                        <FontAwesomeIcon
                                            icon={faDiscord}
                                            size="2x"
                                        />
                                    </NavLink>
                                    <UncontrolledTooltip
                                        placement="top"
                                        target={"discord"}
                                    >
                                        Discord
                                    </UncontrolledTooltip>
                                </NavItem>
                            </Nav>
                        </Container>
                    </Navbar>
                </div>
            </>
        );
    }
}

export default connect(null, { showFeedback })(Footer);
