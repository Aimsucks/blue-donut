import { SHOW_FEEDBACK, HIDE_FEEDBACK, SEND_FEEDBACK } from "../actions/types";

const initialState = {
    show: false,
    form: {}
};

export default function(state = initialState, action) {
    switch (action.type) {
        case SHOW_FEEDBACK:
            return {
                show: true
            };
        case HIDE_FEEDBACK:
            return {
                show: false
            };
        case SEND_FEEDBACK:
            return {
                ...state,
                form: action.payload
            };
        default:
            return state;
    }
}
