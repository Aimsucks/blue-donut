import { GET_LIST_RECENTS } from "../actions/types.js";

const initialState = {
    recents: []
};

export default function(state = initialState, action) {
    switch (action.type) {
        case GET_LIST_RECENTS:
            return {
                ...state,
                recents: action.payload
            };
        default:
            return state;
    }
}
