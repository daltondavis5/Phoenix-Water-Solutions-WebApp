import {FETCH_UTILITIES} from './types'
import axios from 'axios'
import { FETCH_POSTS } from '../../../../../react-redux-test/src/actions/types'

export const fetchUtilities = () => (dispatch) => {
  axios.get("/api/utility")
  .then(({data}) => {
    dispatch({
      type: FETCH_UTILITIES,
      payload: data,
    })
  })
}