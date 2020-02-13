import { GET_ROUTE } from "../actions/types.js";

const initialState = {
    route: {}
};

export default function(state = initialState, action) {
    switch (action.type) {
        case GET_ROUTE:
            return {
                ...state,
                route: action.payload
            };
        default:
            return state;
    }
}
