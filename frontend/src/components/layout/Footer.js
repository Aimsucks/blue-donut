import React from "react";

import { Navbar, Container, Nav, NavItem, NavLink } from "reactstrap";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGithub, faDiscord } from "@fortawesome/free-brands-svg-icons";

export class Footer extends React.Component {
    render() {
        return (
            <>
                <div className="fixed-bottom">
                    <Navbar dark>
                        <Container>
                            <Nav className="mr-auto">
                                <NavItem className="text-muted">
                                    Made by{" "}
                                    <a
                                        className="text-info"
                                        href="https://evewho.com/character/2113697818"
                                    >
                                        Aimsucks
                                    </a>
                                    with help from
                                    <a
                                        className="text-info"
                                        href="https://evewho.com/character/94944046"
                                    >
                                        Callum Lul
                                    </a>
                                    and
                                    <a
                                        className="text-info"
                                        href="https://evewho.com/character/94854191"
                                    >
                                        Telltak Laellithor
                                    </a>
                                </NavItem>
                            </Nav>
                            <Nav className="ml-auto">
                                <NavItem>
                                    <NavLink
                                        className="text-muted px-2"
                                        href="https://github.com/Aimsucks/blue-donut"
                                    >
                                        <FontAwesomeIcon
                                            icon={faGithub}
                                            size="2x"
                                        />
                                    </NavLink>
                                </NavItem>
                                <NavItem>
                                    <NavLink
                                        className="text-muted px-2"
                                        href="https://discord.gg/UCK8ase"
                                    >
                                        <FontAwesomeIcon
                                            icon={faDiscord}
                                            size="2x"
                                        />
                                    </NavLink>
                                </NavItem>
                            </Nav>
                        </Container>
                    </Navbar>
                </div>
            </>
        );
    }
}

export default Footer;
