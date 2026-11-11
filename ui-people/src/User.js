import React from 'react';

import { connect } from "react-redux";
import { Badge } from "react-bootstrap";
import { fetchUpdateUser } from "./redux/actions";

const User = ({ userInfo, fetchUpdateUser }) => (
    <li onClick={() => fetchUpdateUser(userInfo.person_id, !userInfo.flag)} style={{ cursor: "pointer" }}>
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
            <Badge bg="secondary">is being updated</Badge>
        );
    } else if (userInfo.flag) {
        return <Badge bg="success">✔ Enabled</Badge>;
    } else {
        return <Badge bg="danger">✘ Disabled</Badge>;
    }
};

export default connect(
    null,
    { fetchUpdateUser }
)(User);
