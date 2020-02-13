import React, { Component } from "react";

import Select from "react-select";
import { customStyles } from "../../common/SelectStyle";

import { Input } from "reactstrap";

// Working on this as a replacement for all 3 select components
// https://stackoverflow.com/questions/48407785/react-pass-function-to-child-component
// Going to pass in all the data as props and be able to use it 3 different ways

export class SystemSelect extends Component {
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
                {this.props.systems.length ? (
                    <Select
                        id="SystemSelectSystem"
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
                        placeholder="SystemSelect"
                    />
                ) : (
                    <Input name="system" placeholder="SystemSelect" />
                )}
            </>
        );
    }
}

export default SystemSelect;
