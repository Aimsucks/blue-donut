import axios from "axios";
import { returnErrors } from "./messages";
import {
    GET_LIST_POPULAR,
    GET_LIST_FAVORITES,
    POST_LIST_FAVORITES,
    GET_LIST_RECENTS
} from "./types";
import Cookies from "js-cookie";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export const getPopular = () => dispatch => {
    axios
        .get("/api/popular/")
        .then(res => {
            dispatch({
                type: GET_LIST_POPULAR,
                payload: res.data
            });
        })
        .catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status));
        });
};

export const getFavorites = () => dispatch => {
    axios
        .get("/api/favorites/")
        .then(res => {
            dispatch({
                type: GET_LIST_FAVORITES,
                payload: res.data
            });
        })
        .catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status));
        });
};

export const sendFavorites = favorites => dispatch => {
    axios
        .post("/api/favorites/", favorites, {
            headers: {
                "X-CSRFTOKEN": Cookies.get("csrftoken")
            }
        })
        .then(res => {
            dispatch({
                type: POST_LIST_FAVORITES,
                payload: res.data
            });
        })
        .catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status));
        });
};

export const getRecents = () => dispatch => {
    axios
        .get("/api/recents/")
        .then(res => {
            dispatch({
                type: GET_LIST_RECENTS,
                payload: res.data
            });
        })
        .catch(err => {
            dispatch(returnErrors(err.response.data, err.response.status));
        });
};
