import { SEND_REPORT } from "../actions/types.js";

const initialState = {
    report: {}
};

export default function (state = initialState, action) {
    switch (action.type) {
        case SEND_REPORT:
            return {
                ...state,
                report: action.payload
            };
        default:
            return state;
    }
}
