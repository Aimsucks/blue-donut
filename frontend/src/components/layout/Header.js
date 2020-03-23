import React from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";

import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink as BootstrapNavLink,
    Container
} from "reactstrap";

import { Link, NavLink } from "react-router-dom";

import Account from "./Account";

export class Header extends React.Component {
    constructor(props) {
        super(props);

        this.toggle = this.toggle.bind(this);
        this.state = {
            isOpen: false
        };
    }

    static propTypes = {
        status: PropTypes.object.isRequired
    };

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
                        <Link className="navbar-brand" to="/">
                            Blue Donut
                        </Link>
                        <NavbarToggler onClick={this.toggle} />
                        <Collapse isOpen={this.state.isOpen} navbar>
                            <Nav className="mr-auto" navbar>
                                <NavItem>
                                    <NavLink to="/planner" className="nav-link">
                                        Route Planner
                                    </NavLink>
                                </NavItem>
                                <NavItem>
                                    <NavLink
                                        to="/scanner"
                                        className="nav-link disabled"
                                    >
                                        Scans
                                    </NavLink>
                                </NavItem>
                                <NavItem>
                                    <NavLink
                                        to="/appraisal"
                                        className="nav-link disabled"
                                        disabled
                                    >
                                        Appraisal
                                    </NavLink>
                                </NavItem>
                                {this.props.status.is_staff && (
                                    <NavItem>
                                        <NavLink
                                            to="/manager"
                                            className="nav-link"
                                        >
                                            Manager
                                        </NavLink>
                                    </NavItem>
                                )}
                            </Nav>
                            <Nav className="ml-auto" navbar>
                                <Account />
                            </Nav>
                        </Collapse>
                    </Container>
                </Navbar>
            </>
        );
    }
}

const mapStateToProps = state => ({
    status: state.status.status
});

export default connect(mapStateToProps)(Header);
