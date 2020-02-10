import axios from "axios";
import { returnErrors } from './messages'
import { GET_STATUS } from "./types";

export const getStatus = () => dispatch => {
    axios
        .get("/api/status/")
        .then(res => {
            dispatch({
                type: GET_STATUS,
                payload: res.data
            });
        })
        .catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status))
        });
}