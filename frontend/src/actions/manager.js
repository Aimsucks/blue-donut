import axios from "axios";
import { createMessage, returnErrors } from "./messages";
import { GET_STATISTICS } from "./types";
import Cookies from "js-cookie";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

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

export const sendBridges = report => dispatch => {
    axios
        .post("/api/bridges/manual/", report, {
            headers: {
                "X-CSRFTOKEN": Cookies.get("csrftoken")
            }
        })
        .then(res => {
            dispatch(createMessage({ msg: res.data }));
        })
        .catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status));
        });
};
