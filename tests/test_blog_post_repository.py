from lib.blog_post_repository import BlogPostRepository
from lib.blog_posts import Post
from lib.blog_comments import Comment

def test_blog_repository_all(db_connection):
    db_connection.seed("seeds/blog.sql")
    repo = BlogPostRepository(db_connection)
    result = repo.all()
    assert result == [
        Post(1, "post1", "content1"),
        Post(2, "post2", "content2"),
        Post(3, "post3", "content3")
    ]

def test_find_post_with_comments(db_connection):
    db_connection.seed("seeds/blog.sql")
    repo = BlogPostRepository(db_connection)
    result = repo.find_with_comments(1)
    assert result == Post(1, 'post1', 'content1', [
        Comment(1, 'comment1', 'claudia', 1),
        Comment(3, 'comment3', 'tim', 1)
    ])