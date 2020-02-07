import React from 'react';
import { connect } from "react-redux";
import User from "./User";


const renderUsers = (users) => (
    <ul>
        { users.map((user, index) => {
            return <User userInfo={user} key={index} />
        }) }
    </ul>
)

const renderNoUser = () => (
    <div>
    No users were loaded. Please, have a look at the README and create some users.
    </div>
)

const Users = function ({ loading, users }) {
    if (loading) {
        return (<div>Users are loading</div>);
    } else {
        if (users.length > 0) {
            return (renderUsers(users));
        } else {
            return (renderNoUser());
        }
    }
};

const mapStateToProps = state => {
    const allIds = state.users.allUserIds;
    const userByIds = state.users.userByIds;
    const allUsers = allIds.map(id => userByIds[id]);
    return {loading: state.users.loading, users: allUsers};
};

export default connect(mapStateToProps)(Users);
