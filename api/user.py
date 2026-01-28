from uuid import uuid4
import json
import os


def load_data(type):
    db_path = os.path.join(os.path.dirname(__file__), "..", "database", f"{type}s.json")
    lecturer_database = open(db_path)

    return json.load(lecturer_database)


def check(type, name, password):
    data = load_data(type)

    user_exists = False
    password_matches = False
    id = False

    for user in data:
        if user_exists:
            break

        if user["name"] == name:
            user_exists = True

            if user["password"] == password:
                password_matches = True
                id = user["id"]

    return {"exists": user_exists, "match": password_matches, "id": id}


def register(type, name, password):
    data = load_data(type)

    data.append({"id": str(uuid4()), "name": name, "password": password})

    db_path = os.path.join(os.path.dirname(__file__), "..", "database", f"{type}s.json")
    with open(db_path, "w") as write_file:
        json.dump(data, write_file)


def get(type, id):
    data = load_data(type)

    for user in data:
        if user["id"] == id:
            return user


def set(type, id, key, value):
    data = load_data(type)

    for user in data:
        if user["id"] == id:
            user[key] = value

    db_path = os.path.join(os.path.dirname(__file__), "..", "database", f"{type}s.json")
    with open(db_path, "w") as write_file:
        json.dump(data, write_file)
