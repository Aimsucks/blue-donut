import axios from "axios";
import { returnErrors } from "./messages";
import { GET_ROUTE } from "./types";

export const getRoute = (data) => dispatch => {
    console.log(data)
    axios
        .get("/api/route/")
        .then(res => {
            dispatch({
                type: GET_ROUTE,
                payload: res.data
            });
        })
        .catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status));
        });
};
