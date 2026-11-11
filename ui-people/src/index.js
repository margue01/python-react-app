import "core-js/stable";
import "regenerator-runtime/runtime";
import React from 'react';
import { createRoot } from 'react-dom/client';

import { Provider } from "react-redux";
import store from "./redux/store";

import './index.css';
import App from "./App";

const rootElement = document.getElementById("root");
createRoot(rootElement).render(
  <Provider store={store}>
    <App />
  </Provider>
);
