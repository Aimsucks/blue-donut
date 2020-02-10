import { GET_STATUS } from '../actions/types'

const initialState = {
    status: false
}

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_STATUS:
            return {
                ...state,
                status: action.payload
            }
        default:
            return state
    }
}