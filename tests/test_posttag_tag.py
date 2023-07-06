from lib.posttag_tag import Tag

def test_construction():
    tag = Tag(1, "happy")
    assert tag.id == 1
    assert tag.name == 'happy'

def test_eq_method():
    tag = Tag(1, "happy")
    tag2 = Tag(1, "happy")
    assert tag == tag2

def test_repr_method():
    tag = Tag(1, "happy")
    assert str(tag) == "Tag(1, happy)"