import axios from "axios";

import { GET_CHARACTERS, UPDATE_ACTIVE } from "./types";

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
        .patch("/api/characters/")
        .then(res => {
            dispatch({
                type: UPDATE_ACTIVE,
                payload: id
            })
        })
        .catch(err => console.log(err));
}
