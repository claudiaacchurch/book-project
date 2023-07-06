from lib.posttag_tag import Tag

class PostTagRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_by_post(self, id):
        results = self._connection.execute('SELECT tags.id, tags.name FROM tags JOIN posts_tags ON tags.id = tag_id'\
                                 ' JOIN posts ON posts_tags.post_id = posts.id'\
                                    ' WHERE posts.id = %s', [id])
        tags = []
        for row in results:
            tag = Tag(row['id'], row['name'])
            tags.append(tag.name)
        print(tags)
        return tags
        