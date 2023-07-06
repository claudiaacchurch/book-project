from lib.posttag_repository import PostTagRepository
from lib.posttag_post import Post
from lib.posttag_tag import Tag

def test_find_by_post(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repo = PostTagRepository(db_connection)
    result = repo.find_by_post(2)
    assert result == ['coding', 'education']
    #[Tag(1, 'coding'), Tag(4, 'education')]