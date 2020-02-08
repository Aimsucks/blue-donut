import axios from "axios";
// import cookie from "react-cookies";

import { GET_CHARACTERS } from "./types";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export const getCharacters = () => dispatch => {
    axios
        .get("/api/characters/")
        .then(res => {
            let current = JSON.parse(localStorage.getItem('activeCharacter'))
            let characters = res.data.map(character => character.character_id)

            if (current == null || !(current in characters)) {
                localStorage.setItem('activeCharacter', res.data[0].character_id)
            }

            dispatch({
                type: GET_CHARACTERS,
                payload: res.data
            });
        })
        .catch(err => console.log(err));
};

// export const updateActive = id => dispatch => {
//     axios
//         .patch("/api/characters/", id, {
//             headers: {
//                 "X-CSRFTOKEN": cookie.load("csrftoken")
//             }
//         })
//         .then(res => {
//             dispatch({
//                 type: UPDATE_ACTIVE,
//                 payload: res.data
//             });
//         })
//         .catch(err => console.log(err));
// };
