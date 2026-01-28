import json
from typing import Literal
from uuid import uuid4
import os

db_path = os.path.join(os.path.dirname(__file__), "..", "database", "modules.json")
with open(db_path) as file:
    data = json.load(file)


def set(
    module_id: str = None,
    trainer_name: str = None,
    language: Literal["python", "java", "c"] = None,
    module_name: str = None,
    level: Literal["beginner", "intermediate", "advanced"] = None,
):
    module_data = data[module_id]

    data[module_id] = {
        "trainer": trainer_name or module_data["trainer"],
        "language": language or module_data["language"],
        "level": level or module_data["level"],
        "name": module_name or module_data["name"],
        "schedule": module_data["schedule"],
        "students": module_data["students"],
    }

    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "modules.json")
    with open(db_path, "w") as write_file:
        json.dump(data, write_file)


def add_schedule(module_id, date_iso):
    data[module_id]["schedule"].append(date_iso)
    data[module_id]["schedule"].sort()

    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "modules.json")
    with open(db_path, "w") as write_file:
        json.dump(data, write_file)


def remove_schedule(module_id, index):
    del data[module_id]["schedule"][index]
db_path = os.path.join(os.path.dirname(__file__), "..", "database", "modules.json")
    with open(db_path
    with open("database/modules.json", "w") as write_file:
        json.dump(data, write_file)


def edit_schedule(module_id, index, date_iso):
    data[module_id]["schedule"][index] = date_iso
    data[module_id]["schedule"].sort()
db_path = os.path.join(os.path.dirname(__file__), "..", "database", "modules.json")
    with open(db_path
    with open("database/modules.json", "w") as write_file:
        json.dump(data, write_file)


def create(
    trainer_id: str,
    language: Literal["python", "java", "c"],
    level: Literal["beginner", "intermediate", "advanced"],
    module_name: str,
):
    uuid = str(uuid4())

    data[uuid] = {
        "trainer": trainer_id,
        "language": language,
        "level": level,
        "name": module_name,
        "schedule": [],
        "students": [],
    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "modules.json")
    with open(db_path

    with open("database/modules.json", "w") as write_file:
        json.dump(data, write_file)

    return uuid


def add_student(module_id, student_id, enrolment_month):
    data[module_id]["students"].append(
        {"id": student_id, "enrolment_month": enrolment_month, "invoice": 1000}
    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "modules.json")
    with open(db_path

    with open("database/modules.json", "w") as write_file:
        json.dump(data, write_file)


def pay_student_invoice(module_id, student_id):
    for student in data[module_id]["students"]:
        if student["id"] == student_id:
    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "modules.json")
    with open(db_path

    with open("database/modules.json", "w") as write_file:
        json.dump(data, write_file)


def remove_student(student_id):
    for module_id, module_data in data.items():
        for index, module_student in enumerate(module_data["students"]):
    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "modules.json")
    with open(db_path= student_id:
                del data[module_id]["students"][index]

    with open("database/modules.json", "w") as write_file:
        json.dump(data, write_file)


def get_filtered_modules(language, level):
    modules = {}

    for module_id, module_data in data.items():
        if module_data["language"] == language and module_data["level"] == level:
            modules[module_id] = module_data

    return modules


def get(module_id):
    return data[module_id]


def db_path = os.path.join(os.path.dirname(__file__), "..", "database", "modules.json")
    with open(db_path
    del data[module_id]

    with open("database/modules.json", "w") as write_file:
        json.dump(data, write_file)
