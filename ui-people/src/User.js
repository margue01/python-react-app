import React from 'react';

import { connect } from "react-redux";
import { fetchUpdateUser } from "./redux/actions";
import { Glyphicon } from "react-bootstrap";

const User = ({ userInfo, fetchUpdateUser }) => (
    <li onClick={() => fetchUpdateUser(userInfo.person_id, !userInfo.flag)}>
        { renderUserData(userInfo) }
    </li>
);

const renderUserData = (userInfo) => (
    <div>
        Name: { userInfo.name } <br/>
        Age: { userInfo.age } <br/>
        Status: { renderStatus(userInfo) } <br/>
    </div>
)
const renderStatus = (userInfo) => {
    if (userInfo.updating) {
        return (
            <span>is being updated</span>
        );
    } else {
        return (
            <span>{ userInfo.flag ? <Glyphicon glyph="ok"/> : <Glyphicon glyph="remove"/> }</span>
        );
    }
};

export default connect(
    null,
    { fetchUpdateUser }
)(User);
