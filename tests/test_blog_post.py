from lib.blog_posts import Post

def test_post_startup():
    post = Post(1, "My post", "my post content")
    assert post.id == 1
    assert post.title == "My post"
    assert post.content == "my post content"

def test_eq_objects_are_same():
    post = Post(1, "My post", "my post content")
    post1 = Post(1, "My post", "my post content")
    assert post == post1

def test_str_formats_correctly():
    post = Post(1, "My post", "my post content")
    assert str(post) == "Post(1, My post, my post content, [])"