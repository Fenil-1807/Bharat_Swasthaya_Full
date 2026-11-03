import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import {
  BrowserRouter,
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  Router,
  RouterProvider,
} from "react-router-dom";

import BharatSwasthyaLanding from "./pages/BharatSwasthyaLanding";

const router = createBrowserRouter(
  createRoutesFromElements(
    <>
      <Route path="/" element={<BharatSwasthyaLanding />} />
    </>,
  ),
);

createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} />,
);
