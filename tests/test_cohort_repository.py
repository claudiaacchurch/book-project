from lib.cohort_repository import CohortRepository
from lib.cohorts import Cohort
from datetime import date
from lib.students import Student

def test_all_cohorts(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repo = CohortRepository(db_connection)
    result = repo.all()
    print([c.__dict__ for c in repo.all()])
    print([c.__dict__ for c in [Cohort(1, 'May', '2023-05-30', []), Cohort(2, 'June', '2023-06-30', [])]])
    assert result == [
        Cohort(1, 'May', date(2023, 5, 30)),
        Cohort(2, 'June', date(2023, 6, 30))
    ]

def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repo = CohortRepository(db_connection)
    result = repo.find_with_students(1)
    assert result == Cohort(1, 'May', date(2023, 5, 30), [
        Student(1, 'claudia', 1),
        Student(2, 'tim', 1)
    ])
