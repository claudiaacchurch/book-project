DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    recipe_name VARCHAR(255),
    cooking_time int,
    rating int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Pizza', 50, 4);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Pasta', 90, 2);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Curry', 20, 5);
INSERT INTO recipes (recipe_name, cooking_time, rating) VALUES ('Salad', 10, 3);
