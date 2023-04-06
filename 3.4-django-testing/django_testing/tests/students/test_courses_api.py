import pytest
from model_bakery import baker
from students.models import Course, Student
from rest_framework.test import APIClient

@pytest.fixture()
def api_class():
    return APIClient()

@pytest.fixture()
def course_bakery():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture()
def student_bakery():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.fixture()
def json_data(student_bakery):
    return {
        "name": "Test Course",
        "students": [student_bakery(_quantity=1)[0].id]
    }


@pytest.mark.django_db
def test_first_course(api_class, course_bakery):
    course = course_bakery(_quantity=1)[0]
    response = api_class.get("/api/v1/courses/{}/".format(course.id))
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == course.name

@pytest.mark.django_db
def test_all_courses(api_class, course_bakery):
    courses = course_bakery(_quantity=10)
    response = api_class.get("/api/v1/courses/")
    assert response.status_code == 200
    data = response.json()
    for i in range(len(courses)):
        assert data[i]['name'] == courses[i].name

@pytest.mark.django_db
def test_filter_id(api_class, course_bakery):
    courses = course_bakery(_quantity=10)
    course = courses[0]
    response = api_class.get("/api/v1/courses/?id={}".format(course.id))
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course.name and data[0]['students'] == list(course.students.values_list('name', flat=True))

@pytest.mark.django_db
def test_filter_name(api_class, course_bakery):
    courses = course_bakery(_quantity=10)
    course = courses[0]
    response = api_class.get("/api/v1/courses/", {"name": course.name})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course.name and data[0]['students'] == list(course.students.values_list('name', flat=True))

@pytest.mark.django_db
def test_create_course(api_class, json_data):
    response = api_class.post("/api/v1/courses/", json_data)
    assert response.status_code == 201
    data = response.json()
    assert data['name'] == json_data['name']

@pytest.mark.django_db
def test_update_course(api_class, course_bakery, json_data):
    course = course_bakery(_quantity=1)[0]
    response = api_class.put("/api/v1/courses/{}/".format(course.id), json_data)
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == json_data['name']

@pytest.mark.django_db
def test_delete_course(api_class, course_bakery):
    course = course_bakery(_quantity=1)[0]
    response = api_class.delete("/api/v1/courses/{}/".format(course.id))
    assert response.status_code == 204