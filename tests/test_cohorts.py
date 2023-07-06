from lib.cohorts import Cohort
from lib.students import Student

def test_cohort_setup():
    cohort = Cohort(1, "June", 2023, [Student(1,'claudia', 1)])
    assert cohort.id == 1
    assert cohort.starting_date == 2023
    assert cohort.students == [Student(1,'claudia', 1)]

def test_eq_method():
    cohort = Cohort(1, "June", 2023, [Student(1,'claudia', 1)])
    cohort2 = Cohort(1, "June", 2023, [Student(1,'claudia', 1)])
    assert cohort == cohort2

def test_repr_method():
    cohort = Cohort(1, "June", 2023, [Student(1,'claudia', 1)])
    assert str(cohort) == "Cohort(1, June, 2023, [Student(1, claudia, 1)])"