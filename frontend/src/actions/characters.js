import axios from "axios";
import cookie from "react-cookies";

import { GET_CHARACTERS, UPDATE_ACTIVE } from "./types";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export const getCharacters = () => dispatch => {
    axios
        .get("/api/characters/")
        .then(res => {
            dispatch({
                type: GET_CHARACTERS,
                payload: res.data
            });
        })
        .catch(err => console.log(err));
};

export const updateActive = id => dispatch => {
    axios
        .patch("/api/characters/", id, {
            headers: {
                "X-CSRFTOKEN": cookie.load("csrftoken")
            }
        })
        .then(res => {
            dispatch({
                type: UPDATE_ACTIVE,
                payload: res.data
            });
        })
        .catch(err => console.log(err));
};
