export const customStyles = {
    control: (provided, state) => ({
        ...provided,
        color: "rgb(208, 204, 197)",
        backgroundColor: "rgb(25,26,27)",
        borderColor: "rgb(95, 95, 95)",
        boxShadow: "none",
        ":focus": {
            ...provided[":focus"],
            borderColor: "#375a7f",
            outline: "none"
        },
        ":active": {
            ...provided[":active"],
            borderColor: "#375a7f",
            outline: "none"
        },
        ":hover": {
            ...provided[":hover"],
            borderColor: "#375a7f",
            outline: "none"
        },
        cursor: "text"
    }),
    input: (provided, state) => ({
        ...provided,
        color: "rgb(208, 204, 197)"
    }),
    placeholder: (provided, state) => ({
        ...provided,
        color: "#999"
    }),
    menuList: (provided, state) => ({
        ...provided,
        backgroundColor: "rgb(25,26,27)",
        borderColor: "rgb(95, 95, 95)",
        borderRadius: "4px",
        borderStyle: "solid",
        borderWidth: "1px"
    }),
    option: (provided, state) => ({
        ...provided,
        color: "rgb(208, 204, 197)",
        backgroundColor: "rgb(25,26,27)",
        ":hover": {
            ...provided[":hover"],
            backgroundColor: "#375a7f"
        },
        padding: "4px 12px"
    }),
    indicatorSeparator: provided => ({
        ...provided,
        display: "none"
    }),
    multiValue: (provided, state) => ({
        ...provided,
        backgroundColor: "#375a7f",
        cursor: "default"
    }),
    multiValueLabel: (provided, state) => ({
        ...provided,
        color: "white",
        paddingLeft: "10px",
        paddingRight: "10px"
    }),
    multiValueRemove: (provided, state) => ({
        ...provided,
        color: "white",
        ":hover": {
            backgroundColor: "#2b4764",
            color: "white"
        }
    }),
    singleValue: (provided, state) => ({
        ...provided,
        color: "white"
    }),
    container: (provided, state) => ({
        ...provided,
        flex: 1
    })
};

export const flexCustomStyles = {
    control: (provided, state) => ({
        ...provided,
        color: "rgb(208, 204, 197)",
        backgroundColor: "rgb(25,26,27)",
        // borderColor: "rgb(95, 95, 95)",
        borderColor: "rgb(95, 95, 95)",
        boxShadow: "none",
        ":focus": {
            ...provided[":focus"],
            borderColor: "#375a7f",
            outline: "none"
        },
        ":active": {
            ...provided[":active"],
            borderColor: "#375a7f",
            outline: "none"
        },
        ":hover": {
            ...provided[":hover"],
            borderColor: "#375a7f",
            outline: "none"
        },
        cursor: "text",
        borderBottomLeftRadius: 0,
        borderTopLeftRadius: 0
    }),
    input: (provided, state) => ({
        ...provided,
        color: "rgb(208, 204, 197)",
    }),
    placeholder: (provided, state) => ({
        ...provided,
        color: state.isDisabled ? "rgb(100,100,100)" : "#999"
    }),
    menuList: (provided, state) => ({
        ...provided,
        backgroundColor: "rgb(25,26,27)",
        borderColor: "rgb(95, 95, 95)",
        borderRadius: "4px",
        borderStyle: "solid",
        borderWidth: "1px"
    }),
    option: (provided, state) => ({
        ...provided,
        color: "rgb(208, 204, 197)",
        backgroundColor: "rgb(25,26,27)",
        ":hover": {
            ...provided[":hover"],
            backgroundColor: "#375a7f"
        },
        padding: "4px 12px"
    }),
    indicatorSeparator: provided => ({
        ...provided,
        display: "none"
    }),
    multiValue: (provided, state) => ({
        ...provided,
        backgroundColor: "#375a7f",
        cursor: "default"
    }),
    multiValueLabel: (provided, state) => ({
        ...provided,
        color: "white",
        paddingLeft: "10px",
        paddingRight: "10px"
    }),
    multiValueRemove: (provided, state) => ({
        ...provided,
        color: "white",
        ":hover": {
            backgroundColor: "#2b4764",
            color: "white"
        },
        cursor: "default"
    }),
    singleValue: (provided, state) => ({
        ...provided,
        color: "white"
    }),
    container: (provided, state) => ({
        ...provided,
        flex: 1
    })
};

export const listsCustomStyles = {
    control: (provided, state) => ({
        ...provided,
        height: "2em",
        minHeight: "2em",
        textAlign: "center",
        color: "rgb(208, 204, 197)",
        backgroundColor: "rgb(25,26,27)",
        borderColor: "rgb(95, 95, 95)",
        boxShadow: "none",
        ":focus": {
            ...provided[":focus"],
            borderColor: "#375a7f",
            outline: "none"
        },
        ":active": {
            ...provided[":active"],
            borderColor: "#375a7f",
            outline: "none"
        },
        ":hover": {
            ...provided[":hover"],
            borderColor: "#375a7f",
            outline: "none"
        },
        cursor: "text"
    }),
    input: (provided, state) => ({
        ...provided,
        color: "rgb(208, 204, 197)",
        padding: "0px",
        textAlign: "center"
    }),
    placeholder: (provided, state) => ({
        ...provided,
        color: "#999",
        textAlign: "center"
    }),
    menuList: (provided, state) => ({
        ...provided,
        backgroundColor: "rgb(25,26,27)",
        borderColor: "rgb(95, 95, 95)",
        borderRadius: "4px",
        borderStyle: "solid",
        borderWidth: "1px"
    }),
    option: (provided, state) => ({
        ...provided,
        color: "rgb(208, 204, 197)",
        backgroundColor: "rgb(25,26,27)",
        ":hover": {
            ...provided[":hover"],
            backgroundColor: "#375a7f"
        },
        padding: "4px 12px"
    }),
    indicatorSeparator: provided => ({
        ...provided,
        display: "none"
    }),
    multiValue: (provided, state) => ({
        ...provided,
        backgroundColor: "#375a7f",
        cursor: "default"
    }),
    multiValueLabel: (provided, state) => ({
        ...provided,
        color: "white",
        paddingLeft: "10px",
        paddingRight: "10px"
    }),
    multiValueRemove: (provided, state) => ({
        ...provided,
        color: "white",
        ":hover": {
            backgroundColor: "#2b4764",
            color: "white"
        }
    }),
    singleValue: (provided, state) => ({
        ...provided,
        color: "white"
    }),
    container: (provided, state) => ({
        ...provided,
        flex: 1,
        textAlign: "center"
    })
};