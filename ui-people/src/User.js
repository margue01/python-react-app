import React from 'react';

import { connect } from "react-redux";
import { enableUser } from "./redux/actions";
import { Glyphicon } from "react-bootstrap";

const User = ({ userInfo, enableUser }) => (
    <li onClick={() => enableUser(userInfo.doc_id)}>
        { userInfo.name } { !userInfo.enable ? <Glyphicon glyph="ok"/> : <Glyphicon glyph="remove"/> }
    </li>
);

export default connect(
    null,
    { enableUser }
)(User);
