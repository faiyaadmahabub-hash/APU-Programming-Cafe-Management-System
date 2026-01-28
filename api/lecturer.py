from uuid import uuid4
import json
import os

db_path = os.path.join(os.path.dirname(__file__), "..", "database", "lecturers.json")
with open(db_path) as lec_file:
    lecturers = json.load(lec_file)


def get(lecturer_id):
    for lecturer in lecturers:
        if lecturer["id"] == lecturer_id:
            return lecturer


def remove_request(lecturer_id, request_id):
    for lecturer in lecturers:
        if lecturer["id"] == lecturer_id:
            del lecturer["requests"][request_id]

    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "lecturers.json")
    with open(db_path, "w") as write_file:
        json.dump(lecturers, write_file)


def check(name, password):
    user_exists = False
    password_matches = False

    for user in lecturers:
        if user_exists:
            break

        if user["name"] == name:
            user_exists = True

            if user["password"] == password:
                password_matches = True

    return {"exists": user_exists, "match": password_matches}


def add_request(lecturer_id, request_id, request_data):
    for lecturer in lecturers:
        if lecturer["id"] == lecturer_id:
            lecturer["requests"][request_id] = request_data

    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "lecturers.json")
    with open(db_path, "w") as write_file:
        json.dump(lecturers, write_file)


def delete_request(lecturer_id, request_id):
    for lecturer in lecturers:
        if lecturer["id"] == lecturer_id:
            del lecturer["requests"][request_id]

    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "lecturers.json")
    with open(db_path, "w") as write_file:
        json.dump(lecturers, write_file)


def change_name(lecturer_id, new_name):
    for lecturer in lecturers:
        if lecturer["id"] == lecturer_id:
            lecturer["name"] = new_name

    with open("database/lecturers.json", "w") as write_file:
        json.dump(lecturers, write_file)


def change_password(lecturer_id, new_password):
    for lecturer in lecturers:
        if lecturer["id"] == lecturer_id:
            lecturer["password"] = new_password

    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "lecturers.json")
    with open(db_path, "w") as write_file:
        json.dump(lecturers, write_file)


def register(name, password):
    lecturers.append(
        {"id": str(uuid4()), "name": name, "password": password, "requests": []}
    )

    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "lecturers.json")
    with open(db_path, "w") as write_file:
        json.dump(lecturers, write_file)
