import React, { Component } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getStatus } from "../../actions/status";
import { getCharacters } from "../../actions/characters";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
    faSignInAlt,
    faSignOutAlt,
    faChevronDown,
    faPlus
} from "@fortawesome/free-solid-svg-icons";

import { NavLink as RouterLink } from "react-router-dom";

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
        characters: PropTypes.array,
        status: PropTypes.object
    };

    componentDidMount() {
        this.props.getStatus()
    }

    componentDidUpdate(prevProps) {
        if (!prevProps.status.logged_in & this.props.status.logged_in == true) {
            this.props.getCharacters();
        }
    }

    render() {
        if (!this.props.status.logged_in) {
            return (
                <>
                    <NavItem>
                        <RouterLink to="/login" className="nav-link">
                            <FontAwesomeIcon className="mr-2" icon={faSignInAlt} />
                            Log in
                        </RouterLink>
                    </NavItem>
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
                            nav
                        >
                            <img
                                src={
                                    this.props.characters.length
                                        ? "https://image.eveonline.com/Character/" +
                                        JSON.parse(localStorage.getItem('activeCharacter')) +
                                        "_32.jpg"
                                        : "https://image.eveonline.com/Character/1_32.jpg"
                                }
                                height="32px"
                                className="avatar mr-2"
                            />
                            <span>
                                {this.props.characters.length
                                    ? this.props.characters.find(o => o.character_id === JSON.parse(localStorage.getItem('activeCharacter'))).name
                                    : "Loading..."}
                            </span>
                            <FontAwesomeIcon
                                className="ml-2"
                                icon={faChevronDown}
                            />
                        </DropdownToggle>
                        <DropdownMenu>
                            {this.props.characters.map(character => (
                                <DropdownItem
                                    key={character.character_id}
                                    disabled={
                                        JSON.parse(localStorage.getItem('activeCharacter')) ===
                                            character.character_id
                                            ? true
                                            : false
                                    }
                                    onClick={
                                        () => { localStorage.setItem('activeCharacter', JSON.stringify(character.character_id)); this.setState({}) }
                                    }
                                >
                                    <img
                                        src={
                                            "https://image.eveonline.com/Character/" +
                                            character.character_id +
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
    characters: state.characters.characters,
    status: state.status.status
});

export default connect(mapStateToProps, { getStatus, getCharacters })(Account);
