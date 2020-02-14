import { GET_LIST_POPULAR } from "../actions/types.js";

const initialState = {
    popular: []
};

export default function(state = initialState, action) {
    switch (action.type) {
        case GET_LIST_POPULAR:
            return {
                ...state,
                popular: action.payload
            };
        default:
            return state;
    }
}
