import { SEND_BRIDGES } from "../actions/types.js";

const initialState = {
    bridges: []
};

export default function (state = initialState, action) {
    switch (action.type) {
        case SEND_BRIDGES:
            return {
                ...state,
                bridges: action.payload
            };
        default:
            return state;
    }
}
