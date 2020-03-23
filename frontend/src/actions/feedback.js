import { SHOW_FEEDBACK, HIDE_FEEDBACK, SEND_FEEDBACK } from "./types";
import axios from "axios";
import { createMessage, returnErrors } from "./messages";
import Cookies from "js-cookie";

export const showFeedback = () => dispatch => {
    dispatch({
        type: SHOW_FEEDBACK
    });
};

export const hideFeedback = () => dispatch => {
    dispatch({
        type: HIDE_FEEDBACK
    });
};

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export const sendFeedback = feedback => dispatch => {
    axios
        .post("/api/feedback/", feedback, {
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
