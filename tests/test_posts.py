from lib.posts import Post

def test_post_construction():
    post = Post(1, 'My Post', 'content', 10, 2)
    assert post.id == 1
    assert post.title == 'My Post'
    assert post.content == 'content'
    assert post.views == 10
    assert post.user_account_id == 2

def test_post_eq():
    post = Post(1, 'My Post', 'content', 10, 2)
    post2 = Post(1, 'My Post', 'content', 10, 2)
    assert post == post2

def test_str_format():
    post = Post(1, 'My Post', 'content', 10, 2)
    assert str(post) == "Post(1, My Post, content, 10, 2)" 