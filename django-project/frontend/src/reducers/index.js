import { combineReducers } from "redux";
import errors from "./errors";
import messages from "./messages";

export default combineReducers({
  errors,
  messages,
});
