import React, { Component } from "react";

// import WindowedSelect, { createFilter } from "react-windowed-select";
import Select from "react-select";
import { customStyles } from "../../common/SelectStyle";

import { Input } from "reactstrap";

export class Avoid extends Component {
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
                        id="excludedSystems"
                        name="avoid"
                        isMulti
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
                        placeholder="Excluded systems"
                    />
                ) : (
                    <Input
                        name="excludedSystem"
                        placeholder="Excluded systems"
                    />
                )}
            </>
        );
    }
}

export default Avoid;
