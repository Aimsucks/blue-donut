import React, { Component } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";

import Select from "react-select";
import { customStyles } from "./SelectStyle";

import { Input } from "reactstrap";

/*
In order for this to function, it needs to be passed the props:
- name (string)
- selectedOption (state)
- onSelectChange (function)
- style (from SelectStyle.js) if you want to override the default
- placeholder (string)
- isDisabled (state/bool)
- multiple (bool)
*/

export class SystemSelect extends Component {
    constructor(props) {
        super(props);
        this.state = {
            showOptions: false,
            selectedOption: null
        };
    }

    static propTypes = {
        systems: PropTypes.array.isRequired
    };

    onInputChange = typedOption => {
        if (typedOption.length > 2) {
            this.setState({ showOptions: true });
        } else {
            this.setState({ showOptions: false });
        }
    };

    onChange = selectedOption => {
        this.setState({ selectedOption }, () =>
            console.log(`Option selected: ${this.state.selectedOption}`)
        );
    };

    render() {
        const { selectedOption } = this.state;
        return (
            <>
                {this.props.systems.length ? (
                    <Select
                        id={this.props.name + "Select"}
                        name={this.props.name}
                        // value={this.props.selectedOption}
                        value={selectedOption}
                        options={
                            this.state.showOptions
                                ? this.props.systems.map(t => ({
                                      value: t,
                                      label: t
                                  }))
                                : []
                        }
                        // onChange={this.props.onSelectChange}
                        onChange={this.onChange}
                        onInputChange={this.onInputChange}
                        components={{
                            DropdownIndicator: () => null
                        }}
                        styles={
                            this.props.style ? this.props.style : customStyles
                        }
                        openMenuOnClick={false}
                        noOptionsMessage={() =>
                            this.state.showOptions
                                ? "Didn't find any systems"
                                : "Not enough characters"
                        }
                        placeholder={this.props.placeholder}
                        isDisabled={this.props.isDisabled}
                        multiple={this.props.multiple}
                    />
                ) : (
                    <Input
                        name={this.props.name}
                        placeholder={this.props.placeholder}
                    />
                )}
            </>
        );
    }
}

const mapStateToProps = state => ({
    systems: state.map.systems
});

export default connect(mapStateToProps)(SystemSelect);
