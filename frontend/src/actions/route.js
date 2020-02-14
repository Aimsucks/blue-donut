import axios from "axios";
import { returnErrors } from "./messages";
import { GET_ROUTE, CONFIRM_ROUTE } from "./types";
import Cookies from "js-cookie";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export const getRoute = plan => dispatch => {
    axios
        .post("/api/route/", plan, {
            headers: {
                "X-CSRFTOKEN": Cookies.get("csrftoken")
            }
        })
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

export const sendRoute = plan => dispatch => {
    axios
        .post("/api/route/confirm/", plan, {
            headers: {
                "X-CSRFTOKEN": Cookies.get("csrftoken")
            }
        })
        .then(res => {
            console.log(res.data);
            dispatch(createMessage({ sendRoute: res.data }));
            dispatch({
                type: CONFIRM_ROUTE,
                payload: res.data
            });
        })
        .catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status));
        });
};
