import { GET_CHARACTERS } from "../actions/types.js";

const initialState = {
    characters: []
};

export default function(state = initialState, action) {
    switch (action.type) {
        case GET_CHARACTERS:
            return {
                ...state,
                characters: action.payload
            };
        default:
            return state;
    }
}
