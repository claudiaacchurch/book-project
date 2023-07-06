from lib.blog_posts import Post
from lib.blog_comments import Comment

class BlogPostRepository:
    
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            post = Post(row['id'], row['title'], row['content'])
            posts.append(post)
        return posts
    
    def find_with_comments(self, id):
        rows = self._connection.execute('SELECT posts.id AS post_id, posts.title, posts.content AS post_content, '\
                                        'comments.id, comments.content, comments.author_name, comments.post_id '\
                                        'FROM posts JOIN comments ON comments.post_id = posts.id '\
                                            'WHERE comments.post_id = 1')
        comments = []
        for row in rows:
            comment = Comment(row['id'], row['content'], row['author_name'], row['post_id'])
            comments.append(comment)
        return Post(rows[0]['post_id'], rows[0]['title'], rows[0]['post_content'], comments)

        