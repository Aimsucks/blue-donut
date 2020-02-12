import React, { Component } from "react";

// import WindowedSelect, { createFilter } from "react-windowed-select";
import Select from "react-select";
import { customStyles } from "../../common/SelectStyle";

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
            showOptions: false
        };
    }

    handleInputChange = typedOption => {
        if (typedOption.length > 2) {
            this.setState({ showOptions: true });
        } else {
            this.setState({ showOptions: false });
        }
    };
    render() {
        const { selectedOption } = this.state;
        return (
            <>
                <InputGroup>
                    <InputGroupAddon addonType="prepend">
                        <InputGroupText className="px-1" style={checkboxStyle}>
                            <CustomInput
                                className="ml-2 pl-4"
                                type="checkbox"
                                id="originEnable"
                                name="Origin"
                            />
                        </InputGroupText>
                    </InputGroupAddon>
                    {this.props.systems.length ? (
                        <Select
                            id="originSystem"
                            name="to"
                            value={selectedOption}
                            options={
                                this.state.showOptions
                                    ? this.props.systems.map(t => ({
                                          value: t,
                                          label: t
                                      }))
                                    : []
                            }
                            onChange={this.handleChange}
                            onInputChange={this.handleInputChange}
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
                            placeholder="Origin"
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
