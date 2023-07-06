from lib.students import Student

def test_student_setup():
    student = Student(1, 'claudia', 1)
    assert student.id == 1
    assert student.name == 'claudia'
    assert student.cohort_id == 1

def test_student_equals_student():
    student = Student(1, 'claudia', 1)
    student2 = Student(1, 'claudia', 1)
    assert student == student2

def test_string_format():
    student = Student(1, 'claudia', 1)
    assert str(student) == "Student(1, claudia, 1)"
