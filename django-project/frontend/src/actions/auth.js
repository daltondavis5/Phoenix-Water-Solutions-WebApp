import axios from "axios";
import {
  USER_LOADING,
  USER_LOADED,
  AUTH_ERROR,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  LOGOUT_SUCCESS,
} from "./types";
import { returnErrors, createMessage } from "./messages";

// check token and load user
export const loadUser = () => (dispatch, getState) => {
  // User Loading
  dispatch({ type: USER_LOADING });

  axios
    .get("/api/auth/user", getConfig(getState))
    .then((res) => {
      dispatch({
        type: USER_LOADED,
        payload: res.data,
      });
    })
    .catch((err) => {
      dispatch(returnErrors(err.response.data, err.response.status));
      dispatch({
        type: AUTH_ERROR,
      });
    });
};

// login user
export const loginUser = (username, password) => (dispatch, getState) => {
  const body = JSON.stringify({ username, password });

  axios
    .post("/api/auth/login", body, getConfig(getState))
    .then((res) => {
      dispatch(createMessage({ msg: "Login Successful!" }));
      dispatch({
        type: LOGIN_SUCCESS,
        payload: res.data,
      });
    })
    .catch((err) => {
      dispatch(returnErrors(err.response.data, err.response.status));
      dispatch({
        type: LOGIN_FAIL,
      });
    });
};

// register user
export const registerUser = (username, email, password) => (
  dispatch,
  getState
) => {
  const body = JSON.stringify({ username, email, password });

  axios
    .post("/api/auth/register", body, getConfig(getState))
    .then((res) => {
      dispatch(createMessage({ msg: "User Registered Successful!" }));
      dispatch({
        type: REGISTER_SUCCESS,
        payload: res.data,
      });
    })
    .catch((err) => {
      dispatch(returnErrors(err.response.data, err.response.status));
      dispatch({
        type: REGISTER_FAIL,
      });
    });
};

// logout user
export const logoutUser = () => (dispatch, getState) => {
  axios
    .post("/api/auth/logout", null, getConfig(getState))
    .then((res) => {
      dispatch(createMessage({ msg: "Logged out Successfully!" }));
      dispatch({
        type: LOGOUT_SUCCESS,
      });
    })
    .catch((err) => {
      dispatch(returnErrors(err.response.data, err.response.status));
    });
};

// helper function
export const getConfig = (getState) => {
  // Get token
  const token = getState().auth.token;

  // Headers
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  if (token) {
    config.headers["Authorization"] = `Token ${token}`;
  }

  return config;
};
