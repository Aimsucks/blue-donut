import { GET_SYSTEMS } from "../actions/types.js";

const initialState = {
    systems: []
};

export default function(state = initialState, action) {
    switch (action.type) {
        case GET_SYSTEMS:
            return {
                ...state,
                systems: action.payload
            };
        default:
            return state;
    }
}
