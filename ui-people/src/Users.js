import React from 'react';
import { connect } from "react-redux";
import User from "./User";

const Users = ({ users }) => (
    <ul>
        {users.map((user, index) => {
            return <User userInfo={user} key={index} />
        })}
    </ul>
);

const mapStateToProps = state => {
    const allIds = state.users.allUserIds;
    const userByIds = state.users.userByIds;
    const allUsers = allIds.map(id => userByIds[id]);
    return {users: allUsers};
};

export default connect(mapStateToProps)(Users);
