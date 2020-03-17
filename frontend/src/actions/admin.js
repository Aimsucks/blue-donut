import axios from "axios";
import { returnErrors } from "./messages";
import { GET_STATISTICS } from "./types";

export const getStatistics = () => dispatch => {
    axios
        .get("/api/statistics/")
        .then(res => {
            dispatch({
                type: GET_STATISTICS,
                payload: res.data
            });
        })
        .catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status));
        });
};
