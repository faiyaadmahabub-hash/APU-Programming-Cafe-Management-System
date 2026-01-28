from uuid import uuid4
import json
import os


db_path = os.path.join(os.path.dirname(__file__), "database", "students.json")
with open(db_path) as f:
    students = json.load(f)


def changePassword(student_id, new_password):
    for student in students:
        if student["id"] == student_id:
            student["password"] = new_password

    db_path = os.path.join(os.path.dirname(__file__), "database", "students.json")
    with open(db_path, "w") as file:
        json.dump(students, file)


def changeContact(student_id, new_contact):
    for student in students:
        if student["id"] == student_id:
            student["contact_number"] = new_contact
    db_path = os.path.join(os.path.dirname(__file__), "database", "students.json")
    with open(db_path, "w") as file:
        json.dump(students, file)


def viewShedule(student_id):
    pass


def request(student_id, module, level):
    request_id = str(uuid4())
    request_data = {
        "student_id": student_id,
        "module_name": module,
        "level": level,
        "status": "pending"
    }

    for student in students:
        if student["id"] == student_id:
            student["requests"][request_id] = request_data
db_path = os.path.join(os.path.dirname(__file__), "database", "students.json")
    with open(db_path
    with open("students.json", "w") as file:
        json.dump(students, file)

    return request_id


def show_request_status(student_id):
    for student in students:
        if student["id"] == student_id:
            for i, requests in enumerate(list(student["requests"].values())):
                print(f"{i+1}. Module: {requests["module_name"]}, Level: {requests["level"]}, Status: {requests["status"]}")



def delete_requests(student_id, request_id):
    for student in students:
        if student["id"] == student_id:
            for request in (list(student["requests"].values())):
                if request["status"] == "pending":
                    db_path = os.path.join(os.path.dirname(__file__), "database", "students.json")
                    with open(db_pathequest_id]
                    with open("students.json", "w") as file:
                        json.dump(students, file)
                else:
                    pending = False
                    return pending


def get(student_id):
    for student in students:
        if student["id"] == student_id:
            return student