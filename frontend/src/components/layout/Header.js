import React from "react";

import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink,
    Container
} from "reactstrap";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSignInAlt } from "@fortawesome/free-solid-svg-icons";

export class Header extends React.Component {
    constructor(props) {
        super(props);

        this.toggle = this.toggle.bind(this);
        this.state = {
            isOpen: false
        };
    }

    toggle() {
        this.setState({
            isOpen: !this.state.isOpen
        });
    }

    render() {
        return (
            <>
                <Navbar color="primary" dark expand="md">
                    <Container>
                        <NavbarBrand href="/">Blue Donut</NavbarBrand>
                        <NavbarToggler onClick={this.toggle} />
                        <Collapse isOpen={this.state.isOpen} navbar>
                            <Nav className="mr-auto" navbar>
                                <NavItem>
                                    <NavLink href="/map/region/">
                                        Route Planner
                                    </NavLink>
                                </NavItem>
                                <NavItem>
                                    <NavLink disabled href="">
                                        Scans
                                    </NavLink>
                                </NavItem>
                                <NavItem>
                                    <NavLink disabled href="">
                                        Appraisal
                                    </NavLink>
                                </NavItem>
                            </Nav>
                            <Nav className="ml-auto" navbar>
                                <NavItem>
                                    <NavLink href="">
                                        <FontAwesomeIcon
                                            className="mr-2"
                                            icon={faSignInAlt}
                                        />
                                        Log in
                                    </NavLink>
                                </NavItem>
                            </Nav>
                        </Collapse>
                    </Container>
                </Navbar>
            </>
        );
    }
}

export default Header;
