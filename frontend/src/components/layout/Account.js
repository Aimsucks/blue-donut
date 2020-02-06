import React, { Component } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getCharacters } from "../../actions/characters";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
    faSignInAlt,
    faSignOutAlt,
    faChevronDown,
    faPlus
} from "@fortawesome/free-solid-svg-icons";

import {
    NavItem,
    NavLink,
    UncontrolledDropdown,
    DropdownMenu,
    DropdownToggle,
    DropdownItem
} from "reactstrap";

export class Account extends Component {
    static propTypes = {
        characters: PropTypes.array
    };

    componentDidMount() {
        this.props.getCharacters();
    }

    render() {
        if (!this.props.characters) {
            return (
                <>
                    <NavLink href="/auth/login/">
                        <FontAwesomeIcon className="mr-2" icon={faSignInAlt} />
                        Log in
                    </NavLink>
                </>
            );
        }

        return (
            <>
                <NavItem className="mr-3">
                    <UncontrolledDropdown>
                        <DropdownToggle
                            tag="a"
                            type="button"
                            className="nav-link py-1 mr-2"
                        >
                            <img
                                src="https://image.eveonline.com/Character/2113697818_32.jpg"
                                height="32px"
                                className="avatar mr-2"
                            />
                            <span>Aimsucks</span>
                            <FontAwesomeIcon
                                className="ml-2"
                                icon={faChevronDown}
                            />
                        </DropdownToggle>
                        <DropdownMenu>
                            {this.props.characters.map(character => (
                                <DropdownItem key={character.id}>
                                    <img
                                        src={
                                            "https://image.eveonline.com/Character/" +
                                            character.id +
                                            "_32.jpg"
                                        }
                                        height="24px"
                                        className="avatar mr-2"
                                    />
                                    <span>{character.name}</span>
                                </DropdownItem>
                            ))}
                            <DropdownItem href="/auth/login/">
                                <FontAwesomeIcon
                                    className="ml-1 mr-2"
                                    icon={faPlus}
                                />
                                <span className="ml-1">Add character</span>
                            </DropdownItem>
                        </DropdownMenu>
                    </UncontrolledDropdown>
                </NavItem>
                <NavItem>
                    <NavLink href="/auth/logout/">
                        <FontAwesomeIcon className="mr-2" icon={faSignOutAlt} />
                        Log out
                    </NavLink>
                </NavItem>
            </>
        );
    }
}

const mapStateToProps = state => ({
    characters: state.characters.characters
});

export default connect(mapStateToProps, { getCharacters })(Account);
