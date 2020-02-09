import fetch from 'cross-fetch'
import { GET_USERS, GET_USERS_DONE, ENABLE_USER, ENABLE_USER_DONE } from "./actionTypes";

const APP_PEOPLE_URL = 'http://localhost:8003/app/people'

export const getUsers = () => ({
  type: GET_USERS
});

export const getUsersDone = (users) => ({
  type: GET_USERS_DONE,
  payload: users
});

export const enableUser = id => ({
  type: ENABLE_USER,
  payload: { id }
});

export const enableUserDone = id => ({
  type: ENABLE_USER_DONE,
  payload: { id }
});

export function fetchUsers() {
  return function(dispatch) {
    dispatch(getUsers());
    return fetch(`${APP_PEOPLE_URL}`)
      .then(
        response => response.json(),
        error => console.log('An error occurred while fecthing users.', error)
      )
      .then(json =>
        dispatch(getUsersDone(json))
      )
  }
}

export function fetchUpdateUser(id, flag) {
  return function(dispatch) {
    dispatch(enableUser(id));
    const data = { flag: flag }
    return fetch(`${APP_PEOPLE_URL}/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(
        response => response.json(),
        error => console.log('An error occurred while updating a user.', error)
      )
      .then(() =>
        dispatch(enableUserDone(id))
      )
  }
}
