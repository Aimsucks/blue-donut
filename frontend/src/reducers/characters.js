import { GET_CHARACTERS, UPDATE_ACTIVE } from "../actions/types.js";

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
        case UPDATE_ACTIVE:
            return{
                ...state,
                characters: action.payload
            }
        default:
            return state;
    }
}
