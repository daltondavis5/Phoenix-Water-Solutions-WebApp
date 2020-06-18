import { FETCH_UTILITIES, PROVIDER_ADD_SUCCESS } from "./types";
import axios from "axios";

export const fetchUtilities = () => (dispatch) => {
  axios.get("/api/utility").then(({ data }) => {
    dispatch({
      type: FETCH_UTILITIES,
      payload: data,
    });
  });
};

// make a POST call to add provider
export const addProvider = (name, utility_provider) => (dispatch) => {
  const body = JSON.stringify({ name, utility_provider });
  axios.post("/api/provider", body, getConfig()).then((res) => {
    dispatch({
      type: PROVIDER_ADD_SUCCESS,
      payload: res.data,
    });
  });
};

// request config builder
export const getConfig = () => {
  // Headers
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  return config;
};
