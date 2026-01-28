import json
from uuid import uuid4

students = json.load(open("database/students.json"))


def change_password(student_id, new_password):
    for student in students:
        if student["id"] == student_id:
            student["password"] = new_password

    with open("database/students.json", "w") as write_file:
        json.dump(students, write_file)


def change_contact(student_id, new_contact):
    for student in students:
        if student["id"] == student_id:
            student["contact_number"] = new_contact

    with open("database/students.json", "w") as write_file:
        json.dump(students, write_file)


def change_address(student_id, new_address):
    for student in students:
        if student["id"] == student_id:
            student["address"] = new_address

    with open("database/students.json", "w") as write_file:
        json.dump(students, write_file)


def get(student_id):
    for student in students:
        if student["id"] == student_id:
            return student


def get_all():
    return students


def pay_invoice(student_id, module_id):
    for student in students:
        if student["id"] == student_id:
            for module in student["modules"]:
                if module["id"] == module_id:
                    module["invoice"] = 0

    with open("database/students.json", "w") as write_file:
        json.dump(students, write_file)


def add_module(student_id, module_id, enrolment_month):
    for student in students:
        if student["id"] == student_id:
            student["modules"].append(
                {"id": module_id, "enrolment_month": enrolment_month, "invoice": 1000}
            )

    with open("database/students.json", "w") as write_file:
        json.dump(students, write_file)


def add_request(student_id, module_type, module_level):
    request_id = str(uuid4())
    request_data = {
        "sender": student_id,
        "status": "pending",
        "module_request_type": module_type,
        "module_request_level": module_level,
    }

    for student in students:
        if student["id"] == student_id:
            student["requests"][request_id] = request_data

    with open("database/students.json", "w") as write_file:
        json.dump(students, write_file)

    return request_id, request_data


def delete_request(student_id, request_id):
    for student in students:
        if student["id"] == student_id:
            del student["requests"][request_id]

    with open("database/students.json", "w") as write_file:
        json.dump(students, write_file)


def delete(student_id):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            del students[index]

    with open("database/students.json", "w") as write_file:
        json.dump(students, write_file)


def register(name, tp_number, contact_number, address, lecturer_id):
    student_id = str(uuid4())

    students.append(
        {
            "id": student_id,
            "lecturer": lecturer_id,
            "name": name,
            "password": "123",
            "tp_number": tp_number,
            "email": f"{tp_number.lower()}@mail.apu.edu.my",
            "contact_number": contact_number,
            "address": address,
            "modules": [],
            "requests": {},
        }
    )

    with open("database/students.json", "w") as write_file:
        json.dump(students, write_file)

    return student_id
