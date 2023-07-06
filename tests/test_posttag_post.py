from lib.posttag_post import Post

def test_post_construction():
    post = Post(1, "hello")
    assert post.id == 1
    assert post.title == "hello"

def test_post_equal_method():
    post = Post(1, "hello")
    post2 = Post(1, "hello")
    assert post == post2

def test_post_str_formats():
    post = Post(1, "hello")
    assert str(post) == "Post(1, hello)"