from lib.cohorts import Cohort
from lib.students import Student

class CohortRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM cohorts')
        cohorts = []
        for row in rows:
            cohort = Cohort(row['id'], row['name'], row['starting_date'])
            cohorts.append(cohort)
        return cohorts

    def find_with_students(self, id):
        rows = self._connection.execute('SELECT cohorts.id AS cohort_id, cohorts.name, cohorts.starting_date,'\
                                 ' students.id, students.name AS students_name, students.cohort_id FROM students JOIN cohorts ON'\
                                    ' students.cohort_id = cohorts.id WHERE cohorts.id = %s', [id])
        students = []
        for row in rows:
            student = Student(row['id'], row['students_name'], row["cohort_id"])
            students.append(student)
        return Cohort(rows[0]['cohort_id'], rows[0]['name'], rows[0]['starting_date'], students)

        