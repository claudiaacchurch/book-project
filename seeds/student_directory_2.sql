DROP TABLE if EXISTS students;
DROP SEQUENCE if EXISTS students_id_seq;

DROP TABLE if EXISTS cohorts;
DROP SEQUENCE if EXISTS cohorts_id_seq;

CREATE SEQUENCE if NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date date
);



CREATE SEQUENCE if NOT EXISTS students_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO cohorts (name, starting_date) VALUES ('May', '2023-05-30');
INSERT INTO cohorts (name, starting_date) VALUES ('June', '2023-06-30');
INSERT INTO students (name, cohort_id) VALUES ('claudia', 1);
INSERT INTO students (name, cohort_id) VALUES ('tim', 1);
INSERT INTO students (name, cohort_id) VALUES ('lucy', 2);

