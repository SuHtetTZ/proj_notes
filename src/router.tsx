import { createBrowserRouter } from "react-router-dom";
import Root from "./Root";
import DashboardLayout from "./Layouts/DashboardLayout";

import Posts from "./pages/Posts";
import CreatePost from "./pages/CreatePost";
import Users from "./Users";
import CreateUser from "./pages/CreateUser";
import LoginPage from "./Login/LoginPage";
import PostDetail from "./pages/PostDetail";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />, // Header
    children: [
      {
        element: <DashboardLayout />, // Sidebar
        children: [
          { index: true, element: <Posts />},
          { path: "posts", element: <Posts />, children: [{
            path: 'detail/:post_id', element: <PostDetail />
          }] },
          { path: "posts/create", element: <CreatePost /> },
          { path: "users", element: <Users /> },
          { path: "users/create", element: <CreateUser /> },
        ],
      },
    ],
  },
  {
    path: "/login",
    element: <LoginPage />,
  },
]);

export default router;
