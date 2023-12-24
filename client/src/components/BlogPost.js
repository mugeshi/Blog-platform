import React, { useState, useEffect } from 'react';

const BlogPostList = () => {
  const [blogPosts, setBlogPosts] = useState([]);

  useEffect(() => {
    // Fetch blog posts from API
    const fetchBlogPosts = async () => {
      try {
        const response = await fetch('https://blog-json-un87.onrender.com/blogs');
        if (!response.ok) {
          throw new Error('Failed to fetch blog posts');
        }

        const data = await response.json();
        setBlogPosts(data);
      } catch (error) {
        console.error(error.message);
      }
    };

    fetchBlogPosts();
  }, []);

  return (
    <div>
      <h2>Blog Posts</h2>
      <ul>
        {blogPosts.map((post) => (
          <li key={post.id}>
            <h3>{post.title}</h3>
            <p>{post.preview}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BlogPostList;
