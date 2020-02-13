import React, { Component } from "react";

// import WindowedSelect, { createFilter } from "react-windowed-select";
import Select from "react-select";
import { flexCustomStyles } from "../../common/SelectStyle";

import {
    Input,
    InputGroup,
    InputGroupAddon,
    InputGroupText,
    CustomInput
} from "reactstrap";

const checkboxStyle = {
    backgroundColor: "rgb(25,26,27)",
    borderColor: "rgb(95, 95, 95)"
};

export class Origin extends Component {
    constructor(props) {
        super(props);
        this.state = {
            showOptions: false,
            isChecked: false,
            selectedOption: null
        };
    }

    onSelectChange = option => {
        this.setState({ selectedOption: option })
    }

    handleInputChange = typedOption => {
        if (typedOption.length > 2) {
            this.setState({ showOptions: true });
        } else {
            this.setState({ showOptions: false });
        }
    };

    handleChange() {
        if (this.state.isChecked == true) {
            this.setState({ selectedOption: null })
        }
        this.setState({ isChecked: !this.state.isChecked })
    }

    render() {
        return (
            <>
                <InputGroup>
                    <InputGroupAddon addonType="prepend">
                        <InputGroupText className="px-1" style={checkboxStyle}>
                            <CustomInput
                                value={this.state.isChecked}
                                onChange={this.handleChange.bind(this)}
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
                            value={this.state.selectedOption}
                            onChange={this.onSelectChange.bind(this)}
                            options={
                                this.state.showOptions
                                    ? this.props.systems.map(t => ({
                                        value: t,
                                        label: t
                                    }))
                                    : []
                            }
                            onInputChange={this.handleInputChange}
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
                            <Input name="system" placeholder="Origin" />
                        )}
                </InputGroup>
            </>
        );
    }
}

export default Origin;
