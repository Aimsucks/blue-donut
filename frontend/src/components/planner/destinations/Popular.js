import React, { Component } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getPopular, sendPopular } from "../../../actions/lists";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEdit, faSave, faTimes } from "@fortawesome/free-solid-svg-icons";

import { ListGroup, ListGroupItem } from "reactstrap";

import Select from "react-select";
import { listsCustomStyles } from "../../common/SelectStyle";

const placeholderList = [1, 2, 3, 4, 5]

export class Popular extends Component {
    constructor(props) {
        super(props);
        this.state = {
            showOptions: false,
            editMode: false,
            popular: [null, null, null, null, null],
            initialUpdate: false
        };
    }

    static propTypes = {
        popular: PropTypes.array.isRequired,
        status: PropTypes.object.isRequired
    };
    componentDidMount() {
        this.props.getPopular();
    }

    componentDidUpdate(prevProps) {
        if (this.props.popular !== prevProps.popular) {
            let popular = this.props.popular.map(t => (t ? { value: t, label: t } : null))
            this.setState({ popular: popular })
        }
    }

    handleIconClick = () => {
        if (this.state.editMode) {
            let popular = this.state.popular.map(t => t ? t.label : null)
            this.props.sendPopular(popular)
        }
        this.setState({ editMode: !this.state.editMode })
    }

    handleClearClick = () => {
        this.setState({ popular: [null, null, null, null, null] })
    }

    handleSelectInputChange = typedOption => {
        if (typedOption.length > 2) {
            this.setState({ showOptions: true });
        } else {
            this.setState({ showOptions: false });
        }
    };

    handleSelectChange = index => value => {
        let popular = [...this.state.popular]
        popular[index] = value
        this.setState({ popular: popular })
    };

    render() {
        return (
            <>
                <ListGroup className="text-center">
                    {this.props.popular ?
                        this.props.popular.map((system, index) => (
                            this.state.editMode ?
                                <ListGroupItem
                                    className="px-1 py-1"
                                    key={index}
                                >
                                    <Select
                                        id={"favoriteInput" + index}
                                        options={
                                            this.state.showOptions
                                                ? this.props.systems.map(t => ({
                                                    value: t,
                                                    label: t
                                                }))
                                                : []
                                        }
                                        onInputChange={
                                            this.handleSelectInputChange
                                        }
                                        onChange={this.handleSelectChange(index)}
                                        components={{
                                            DropdownIndicator: () => null
                                        }}
                                        styles={listsCustomStyles}
                                        openMenuOnClick={false}
                                        noOptionsMessage={() =>
                                            this.state.showOptions
                                                ? "Didn't find any systems"
                                                : "Not enough characters"
                                        }
                                        value={this.state.popular[index]}
                                        placeholder=""
                                    />
                                </ListGroupItem>
                                : <ListGroupItem
                                    tag="a"
                                    href=""
                                    className="py-2"
                                    action
                                    disabled={this.state.popular[index] ? false : true}
                                    key={index}
                                >
                                    {this.state.popular[index] ? this.state.popular[index].label : "N/A"}
                                </ListGroupItem>
                        ))
                        : placeholderList.map(index => (
                            <ListGroupItem
                                tag="a"
                                href=""
                                className="py-2"
                                action
                                disabled
                                key={index}>
                            </ListGroupItem>
                        ))
                    }
                </ListGroup>
                {this.props.status.is_staff ?
                    <div className="d-flex justify-content-around">
                        <div className={this.state.editMode ? "" : "invisible"} onClick={this.handleClearClick}><FontAwesomeIcon icon={this.state.editMode ? faTimes : faEdit} size="sm" className="text-info" /></div>
                        <div><small className="text-muted">Popular</small></div>
                        <div><a className="text-info clickable-link" onClick={this.handleIconClick}><FontAwesomeIcon icon={this.state.editMode ? faSave : faEdit} size="sm" /></a></div>
                    </div>
                    : <div className="text-center"><small className="text-muted">Popular</small></div>}
            </>
        );
    }
}

const mapStateToProps = state => ({
    popular: state.popular.popular,
    status: state.status.status
});

export default connect(mapStateToProps, { getPopular, sendPopular })(Popular);
