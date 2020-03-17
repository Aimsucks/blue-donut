import { GET_STATISTICS } from "../actions/types.js";

const initialState = {
    statistics: {}
};

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_STATISTICS:
            return {
                ...state,
                statistics: action.payload
            };
        default:
            return state;
    }
}
