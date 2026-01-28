import json
from uuid import uuid4
from typing import Literal
import os

db_path = os.path.join(os.path.dirname(__file__), "..", "database", "feedbacks.json")
with open(db_path) as feedbacks_file:
    data = json.load(feedbacks_file)


def create(sender: str, type: Literal["suggestion", "complaint"], message: str):
    feedback_uuid = str(uuid4())

    data[feedback_uuid] = {"sender": sender, "type": type, "message": message}

    db_path = os.path.join(os.path.dirname(__file__), "..", "database", "feedbacks.json")
    with open(db_path, "w") as write_file:
        json.dump(data, write_file)

    return feedback_uuid


def get(feedback_uuid: str):
    return data[feedback_uuid]


def get_all():
    return list(data.values())
