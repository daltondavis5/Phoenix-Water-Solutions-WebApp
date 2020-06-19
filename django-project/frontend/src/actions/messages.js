import { GET_ERRORS, CREATE_MESSAGE } from "./types";

export const createMessage = (msg) => (dispatch) =>
  dispatch({
    type: CREATE_MESSAGE,
    payload: msg,
  });

export const returnErrors = (msg, status) => (dispatch) =>
  dispatch({
    type: GET_ERRORS,
    payload: { msg, status },
  });
