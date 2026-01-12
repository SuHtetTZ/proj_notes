import { Link } from "react-router-dom";

export default function Header() {
  return (
    <nav className="navbar navbar-light bg-light border-bottom px-4">
      <Link to="/" className="navbar-brand fw-bold">
        Bulletin Board
      </Link>

      <div className="ms-auto d-flex align-items-center gap-4">
        <span className="text-muted">Last Login At - 01/01/2025</span>
        <span className="text-muted">Role</span>

        <div className="dropdown">
          <button
            className="btn btn-outline-secondary dropdown-toggle"
            data-bs-toggle="dropdown"
          >
            John Doe
          </button>

          <ul className="dropdown-menu dropdown-menu-end">
            <li>
              <Link className="dropdown-item" to="/profile">
                Profile
              </Link>
            </li>
            <li>
              <hr className="dropdown-divider" />
            </li>
            <li>
              <button className="dropdown-item text-danger">
                Logout
              </button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}
