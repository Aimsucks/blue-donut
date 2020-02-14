import { GET_LIST_FAVORITES } from "../actions/types.js";

const initialState = {
    favorites: []
};

export default function(state = initialState, action) {
    switch (action.type) {
        case GET_LIST_FAVORITES:
            return {
                ...state,
                favorites: action.payload
            };
        default:
            return state;
    }
}
