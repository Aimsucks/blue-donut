import axios from "axios";
import { returnErrors } from "./messages";
import { GET_SYSTEMS } from "./types";

export const getSystems = () => dispatch => {
    axios
        .get("/api/systems/")
        .then(res => {
            dispatch({
                type: GET_SYSTEMS,
                payload: res.data
            });
        })
        .catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status));
        });
};
