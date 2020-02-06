import axios from "axios";

import { GET_CHARACTERS } from "./types";

// GET CHARACTERS
export const getCharacters = () => dispatch => {
    axios
        .get("/auth/check/")
        .then(res => {
            dispatch({
                type: GET_CHARACTERS,
                payload: res.data.characters
            });
        })
        .catch(err => console.log(err));
};
