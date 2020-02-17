import { combineReducers } from "redux";

import characters from "./characters";
import errors from "./errors";
import messages from "./messages";
import status from "./status";
import map from "./map";
import route from "./route";
import popular from "./popular";
import favorites from "./favorites";
import recents from "./recents";
import report from "./report"

export default combineReducers({
    characters,
    errors,
    messages,
    status,
    map,
    popular,
    favorites,
    recents,
    route,
    report
});
