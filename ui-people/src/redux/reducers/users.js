import { ADD_USER, ENABLE_USER } from "../actionTypes";

const initialState = {
  allUserIds: [1,2],
  userByIds: {
      "1": {"name": "name1", "enable": false, "doc_id": 1},
      "2": {"name": "name2", "enable": false, "doc_id": 2},
  }
};

export default function(state = initialState, action) {
  switch (action.type) {
    case ADD_USER: {
      const { id, content } = action.payload;
      return {
        ...state,
        allUserIds: [...state.allUserIds, id],
        userByIds: {
          ...state.byIds,
          [id]: {
            content,
            enable: false
          }
        }
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
            enable: !state.userByIds[id].enable
          }
        }
      };
    }
    default:
      return state;
  }
}
