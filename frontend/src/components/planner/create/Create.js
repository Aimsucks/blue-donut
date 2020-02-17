import React, { Component } from "react";
import queryString from "query-string";
import { withRouter } from "react-router-dom";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getRoute } from "../../../actions/route";
import { sendRecents } from "../../../actions/lists"

import {
    Row,
    Col,
    Form,
    Input,
    Button,
    InputGroup,
    InputGroupAddon,
    InputGroupText,
    CustomInput
} from "reactstrap";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPen } from "@fortawesome/free-solid-svg-icons";

import Select from "react-select";
import { customStyles, flexCustomStyles } from "../../common/SelectStyle";
import Report from "../report/Report";

const checkboxStyle = {
    backgroundColor: "rgb(25,26,27)",
    borderColor: "rgb(95, 95, 95)"
};

export class Create extends Component {
    constructor(props) {
        super(props);
        this.state = {
            showOptions: false,
            isChecked: false,
            selectedOption: null,
            from: null,
            to: null,
            avoid: [],
            confirm: false
        };
    }

    static propTypes = {
        route: PropTypes.object
    };

    componentDidUpdate(prevProps, prevState) {
        const parameters = queryString.parse(this.props.location.search);
        if (prevState.from == null && parameters.from) {
            this.setState({
                from: { value: parameters.from, label: parameters.from }
            });
        }
        if (prevState.to == null && parameters.to) {
            this.setState({
                to: { value: parameters.to, label: parameters.to }
            });
        }
    }

    onChange = name => value => {
        name !== "avoid"
            ? this.setState({ [name]: value })
            : this.setState({ [name]: value });
    };

    handleConfirmButton = () => {
        this.setState({ confirm: true });
    };

    onSubmit = e => {
        e.preventDefault();
        let character = localStorage.getItem("activeCharacter");
        let { from, to, avoid, confirm } = this.state;
        if (avoid) avoid = avoid.map(a => a.value);
        if (from) from = from.value;
        to = to ? to.value : null;
        const plan = { character, from, to, avoid, confirm };
        this.props.getRoute(plan)
        if (confirm && to) {
            this.props.sendRecents({ to: to })
        }
        this.setState({ confirm: false });
    }

    handleSelectInputChange = typedOption => {
        if (typedOption.length > 2) {
            this.setState({ showOptions: true });
        } else {
            this.setState({ showOptions: false });
        }
    };

    handleCheckbox() {
        if (this.state.isChecked == true) {
            this.setState({ from: null });
        }
        this.setState({ isChecked: !this.state.isChecked });
    }

    render() {
        const { from, to, avoid } = this.state;
        return (
            <>
                <h2 className="text-center">
                    <FontAwesomeIcon
                        icon={faPen}
                        size="sm"
                        className="mr-2 pb-1"
                    />
                    Create Your Own
                </h2>
                <Form onSubmit={this.onSubmit}>
                    <Row className="px-2">
                        <Col md="6" className="px-1">
                            <InputGroup>
                                <InputGroupAddon addonType="prepend">
                                    <InputGroupText
                                        className="px-1"
                                        style={checkboxStyle}
                                    >
                                        <CustomInput
                                            value={this.state.isChecked}
                                            onChange={this.handleCheckbox.bind(
                                                this
                                            )}
                                            className="ml-2 pl-4"
                                            type="checkbox"
                                            id="originEnable"
                                        />
                                    </InputGroupText>
                                </InputGroupAddon>
                                {this.props.systems.length ? (
                                    <Select
                                        id="originSystem"
                                        name="from"
                                        value={from}
                                        onChange={this.onChange("from")}
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
                                        components={{
                                            DropdownIndicator: () => null
                                        }}
                                        styles={flexCustomStyles}
                                        openMenuOnClick={false}
                                        noOptionsMessage={() =>
                                            this.state.showOptions
                                                ? "Didn't find any systems"
                                                : "Not enough characters"
                                        }
                                        placeholder="Origin"
                                        isDisabled={!this.state.isChecked}
                                    />
                                ) : (
                                        <Input name="from" placeholder="Origin" disabled />
                                    )}
                            </InputGroup>
                        </Col>
                        <Col md="6" className="px-1">
                            {this.props.systems.length ? (
                                <Select
                                    id="destinationSystem"
                                    name="to"
                                    value={to}
                                    options={
                                        this.state.showOptions
                                            ? this.props.systems.map(t => ({
                                                value: t,
                                                label: t
                                            }))
                                            : []
                                    }
                                    onChange={this.onChange("to")}
                                    onInputChange={this.handleSelectInputChange}
                                    components={{
                                        DropdownIndicator: () => null
                                    }}
                                    styles={customStyles}
                                    openMenuOnClick={false}
                                    noOptionsMessage={() =>
                                        this.state.showOptions
                                            ? "Didn't find any systems"
                                            : "Not enough characters"
                                    }
                                    placeholder="Destination"
                                />
                            ) : (
                                    <Input name="to" placeholder="Destination" />
                                )}
                        </Col>
                    </Row>
                    <Row className="px-2 pt-2">
                        <Col md="6" className="px-1">
                            {this.props.systems.length ? (
                                <Select
                                    id="excludedSystems"
                                    name="avoid"
                                    isMulti
                                    value={avoid}
                                    options={
                                        this.state.showOptions
                                            ? this.props.systems.map(t => ({
                                                value: t,
                                                label: t
                                            }))
                                            : []
                                    }
                                    onChange={this.onChange("avoid")}
                                    onInputChange={this.handleSelectInputChange}
                                    components={{
                                        DropdownIndicator: () => null
                                    }}
                                    styles={customStyles}
                                    openMenuOnClick={false}
                                    noOptionsMessage={() =>
                                        this.state.showOptions
                                            ? "Didn't find any systems"
                                            : "Not enough characters"
                                    }
                                    placeholder="Excluded systems"
                                />
                            ) : (
                                    <Input
                                        name="excludedSystem"
                                        placeholder="Excluded systems"
                                    />
                                )}
                        </Col>
                        <Col md="3" className="px-1">
                            <Button
                                name="verify"
                                block
                                color="primary"
                                type="submit"
                            >
                                Verify
                            </Button>
                        </Col>
                        <Col md="3" className="px-1">
                            <Button
                                name="confirm"
                                block
                                color="primary"
                                type="submit"
                                onClick={this.handleConfirmButton}
                            >
                                Generate
                            </Button>
                        </Col>
                    </Row>
                    <Row className="px-2">
                        <Col>
                            <Report />
                        </Col>
                    </Row>
                </Form>
            </>
        );
    }
}

const mapStateToProps = state => ({
    route: state.route.route
});

export default connect(mapStateToProps, { getRoute, sendRecents })(withRouter(Create));
