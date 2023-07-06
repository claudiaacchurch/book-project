from lib.blog_comments import Comment

def test_comment_construction():
    comment = Comment(1, "good comment", "claudia", 4)
    assert comment.id == 1
    assert comment.content == "good comment"
    assert comment.author_name == 'claudia'
    assert comment.post_id == 4

def test_eq_asserts_the_same():
    comment = Comment(1, "good comment", "claudia", 4)
    comment2 = Comment(1, "good comment", "claudia", 4)
    assert comment == comment2

def test_str_formats():
    comment = Comment(1, "good comment", "claudia", 4)
    assert str(comment) == "Comment(1, good comment, claudia, 4)"