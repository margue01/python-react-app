import { GET_USERS, GET_USERS_DONE, ENABLE_USER, ENABLE_USER_DONE } from "../actionTypes";

const initialState = {
  allUserIds: [],
  userByIds: {},
  loading: false
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_USERS: {
      return {
        ...state,
        loading: true
      };
    }
    case GET_USERS_DONE: {
      const users = action.payload;
      const usersById = {}
      users.forEach(user => {
        usersById[user.person_id] = user
      });
      return {
        ...state,
        allUserIds: users.map(item => item.person_id),
        userByIds: usersById
      };
    }
    case ENABLE_USER: {
      const { id } = action.payload;
      return {
        ...state,
        userByIds: {
          ...state.userByIds,
          [id]: {
            ...state.userByIds[id],
            updating: true          }
        }
      };
    }
    case ENABLE_USER_DONE: {
      const { id } = action.payload;
      return {
        ...state,
        userByIds: {
          ...state.userByIds,
          [id]: {
            ...state.userByIds[id],
            flag: !state.userByIds[id].flag,
            updating: false
          }
        }
      };
    }
    default:
      return state;
  }
}
