import { combineReducers } from "redux";

import characters from "./characters";
import errors from "./errors";
import status from "./status";
import map from "./map";

export default combineReducers({
    characters,
    errors,
    status,
    map
});
