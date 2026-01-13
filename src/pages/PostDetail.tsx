import { useNavigate, useParams } from "react-router-dom";
import Modal from "../Components/Modal"

interface Post {
  id: string;
  title: string;
  body: string;
}

const dummyPosts: Record<string, Post> = {
  "1": { id: "1", title: "Hello", body: "First post" },
  "2": { id: "2", title: "World", body: "Second post" },
};

export default function PostDetailModal() {
  const { post_id } = useParams<{ post_id: string }>();
  const navigate = useNavigate();

  if (!post_id) return null;

  const post = dummyPosts[post_id];

  if (!post) return null;

  return (
    <Modal
      isOpen={true}
      onClose={() => navigate("/posts")}
    >
      <h3>{post.title}</h3>
      <p>{post.body}</p>

      <button onClick={() => navigate("/posts")}>
        Close
      </button>
    </Modal>
  );
}
