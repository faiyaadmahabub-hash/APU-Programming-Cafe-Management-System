import json
from uuid import uuid4
from api import module
import os

db_path = os.path.join(os.path.dirname(__file__), "..", "database", "trainers.json")
with open(db_path) as trainers_file:
    data = json.load(trainers_file)


def delete(id):
    deleted_status = False

    for index, user in enumerate(data):
        if user["id"] == id:
            for module_uuid in user["modules"]:
                module.delete(module_uuid)
            del data[index]
            db_path = os.path.join(os.path.dirname(__file__), "..", "database", "trainers.json")
            with open(db_path, "w") as write_file:
                json.dump(data, write_file)
            deleted_status = True
            break

    return deleted_status


def register(name):
    trainer_id = str(uuid4())
    new_trainer = {
        "id": trainer_id,
        "name": name,
        "password": "123",
        "modules": [],
        "feedbacks": [],
    }

    data.append(new_trainer)

    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "trainers.json")
    with open(db_path, "w") as write_file:
        json.dump(data, write_file)

    return trainer_id


def get(trainer_id):
    for trainer in data:
        if trainer["id"] == trainer_id:
            return trainer


def add_module(trainer_id, module_id):
    for trainer in data:
        if trainer["id"] == trainer_id:
            trainer["modules"].append(module_id)
db_path = os.path.join(os.path.dirname(__file__), "..", "database", "trainers.json")
    with open(db_path
    with open("database/trainers.json", "w") as write_file:
        json.dump(data, write_file)


def add_feedback(trainer_id, feedback_id):
    for trainer in data:
        if trainer["id"] == trainer_id:
            trainer["feedbacks"].append(feedback_id)
db_path = os.path.join(os.path.dirname(__file__), "..", "database", "trainers.json")
    with open(db_path
    with open("database/trainers.json", "w") as write_file:
        json.dump(data, write_file)


def change_password(trainer_id, new_password):
    for trainer in data:
        if trainer["id"] == trainer_id:
            trainer["password"] = new_password
db_path = os.path.join(os.path.dirname(__file__), "..", "database", "trainers.json")
    with open(db_path
    with open("database/trainers.json", "w") as write_file:
        json.dump(data, write_file)


def change_name(trainer_id, new_name):
    for trainer in data:
        if trainer["id"] == trainer_id:
    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "trainers.json")
    with open(db_path

    with open("database/trainers.json", "w") as write_file:
        json.dump(data, write_file)
