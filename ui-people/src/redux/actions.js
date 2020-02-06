import { ENABLE_USER } from "./actionTypes";

export const enableUser = id => ({
  type: ENABLE_USER,
  payload: { id }
});
