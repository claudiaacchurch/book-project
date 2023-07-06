-- -------------------------------------------------------------
-- TablePlus 5.3.8(500)
--
-- https://tableplus.com/
--
-- Database: blogdb
-- Generation Time: 2023-07-06 10:09:11.3490
-- -------------------------------------------------------------

DROP TABLE IF EXISTS comments CASCADE;
DROP TABLE IF EXISTS posts CASCADE;

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;

-- Table Definition
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text
);

CREATE SEQUENCE IF NOT EXISTS comments_id_seq;

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content text,
    author_name text,
    post_id int,
    CONSTRAINT fk_post FOREIGN KEY (post_id) 
    REFERENCES posts(id) ON DELETE CASCADE
);

INSERT INTO posts (title, content) VALUES ('post1', 'content1');
INSERT INTO posts (title, content) VALUES ('post2', 'content2');
INSERT INTO posts (title, content) VALUES ('post3', 'content3');
INSERT INTO comments (content, author_name, post_id) VALUES ('comment1', 'claudia', 1);
INSERT INTO comments (content, author_name, post_id) VALUES ('comment2', 'claudia', 2);
INSERT INTO comments (content, author_name, post_id) VALUES ('comment3', 'tim', 1);


