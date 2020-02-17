import axios from "axios";
import { createMessage, returnErrors } from "./messages";
import Cookies from "js-cookie";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export const sendReport = report => dispatch => {
    axios
        .post("/api/report/", report, {
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