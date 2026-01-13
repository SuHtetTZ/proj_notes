import { Link, Outlet, useMatch } from "react-router-dom";

export default function Posts() {
  const match = useMatch("/posts/detail/:post_id");

  return (
    <>
      <h2>Posts</h2>

      <ul>
        <li>
          <Link to="/posts/detail/1">Post 1</Link>
        </li>
        <li>
          <Link to="/posts/detail/2">Post 2</Link>
        </li>
      </ul>

      {/* Outlet renders modal content */}
      <Outlet />

      {/* Optional: blur background when modal open */}
      {match && <div />}
    </>
  );
}

