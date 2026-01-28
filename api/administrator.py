from uuid import uuid4
import json
import os

db_path = os.path.join(os.path.dirname(__file__), "..", "database", "administrators.json")
with open(db_path) as admin_database:
    data = json.load(admin_database)


def check(name, password):
    user_exists = False
    password_matches = False

    for user in data:
        if user_exists:
            break

        if user["name"] == name:
            user_exists = True

            if user["password"] == password:
                password_matches = True

    return {"exists": user_exists, "match": password_matches}


def register(name, password):
    data.append({"id": str(uuid4()), "name": name, "password": password})

    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "administrators.json")
    with open(db_path, "w") as write_file:
        json.dump(data, write_file)
