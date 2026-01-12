import { NavLink, Outlet } from "react-router-dom";

export default function DashboardLayout() {
  return (
    <div className="container-fluid">
      <div className="row" style={{ minHeight: "calc(100vh - 56px)" }}>
        {/* Sidebar */}
        <aside className="col-12 col-md-2 col-lg-2 bg-light border-end p-0">
          <nav className="nav flex-column p-2 gap-1">
            <NavLink to="/posts" className="nav-link">
              Posts
            </NavLink>
            <NavLink to="/posts/create" className="nav-link">
              Create Post
            </NavLink>
            <NavLink to="/users" className="nav-link">
              Users
            </NavLink>
            <NavLink to="/users/create" className="nav-link">
              Create User
            </NavLink>
          </nav>
        </aside>

        {/* Main content */}
        <main className="col p-4">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
