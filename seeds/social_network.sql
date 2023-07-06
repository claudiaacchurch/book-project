DROP TABLE if EXISTS user_accounts;
DROP SEQUENCE if EXISTS user_accounts_id_seq;

CREATE TABLE user_accounts(
    id SERIAL PRIMARY KEY,
    email_address text,
    username text
);

DROP TABLE if EXISTS posts;
DROP SEQUENCE if EXISTS posts_id_seq;

CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    title text,
    content text, 
    views int, 
    user_account_id int,
    constraint fk_user_account foreign key(user_account_id)
    references user_accounts(id) on delete cascade
);