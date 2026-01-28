# TODO: add charges or whatever the fuck, view all students

import sys
import datetime
from api import feedback, module, trainer, student
from utils import select

id = sys.argv[1]

trainer_info = trainer.get(id)


def display_send_feedback():
    feedback_type = select("Feedback type?", ["suggestion", "complaint"])
    message = input("Feedback message: ")

    feedback_id = feedback.create(trainer_info["name"], feedback_type, message)
    trainer.add_feedback(id, feedback_id)

    display_dashboard()


def display_edit_profile():
    print("1. Edit name")
    print("2. Edit password")

    match int(input("\nEnter choice: ")):
        case 1:
            new_name = input("New name: ")
            trainer.change_name(id, new_name)
            print(f"Name successfully changed!")
        case 2:
            new_password = input("New password: ")
            trainer.change_password(id, new_password)
            print(f"Password successfully changed!")

    display_dashboard()


def display_edit_module_name(module_id):
    new_module_name = input("\nEnter new module name: ")
    module.set(module_id, module_name=new_module_name)
    print("Module name successfully changed!")

    display_dashboard()


def display_edit_module_schedule(module_id):
    schedules = module.get(module_id)["schedule"]

    print("\nCurrent schedule:")

    for index, schedule in enumerate(schedules):
        datetime_obj = datetime.datetime.fromisoformat(schedule)
        print(
            f"{index + 1}. {datetime_obj.date().strftime('%A, %b %d %Y')} - {datetime_obj.time().strftime('%I:%M %p')}"
        )

    print("\n1. Edit schedule")
    print("2. Add schedule")
    print("3. Remove schedule")
    print("4. View students")
    print("5. Back")

    def add_schedule():
        date = input("Date (MM/DD/YYYY): ")
        time = input("Time (24 Hour format, HH:MM): ")
        date_iso = datetime.datetime.strptime(
            f"{date} {time}", "%m/%d/%Y %H:%M"
        ).isoformat()

        module.add_schedule(module_id, date_iso)

    def del_schedule():
        schedule_index = int(input("\nEnter schedule index to remove: ")) - 1
        module.remove_schedule(module_id, schedule_index)

    def edit_schedule():
        index = int(input("\nIndex of the schedule to edit: ")) - 1

        date = input("Date (MM/DD/YYYY): ")
        time = input("Time (24 Hour format, HH:MM): ")
        date_iso = datetime.datetime.strptime(
            f"{date} {time}", "%m/%d/%Y %H:%M"
        ).isoformat()

        module.edit_schedule(module_id, index, date_iso)

    match int(input("\nEnter choice: ")):
        case 1:
            edit_schedule()
        case 2:
            add_schedule()
        case 3:
            del_schedule()
        case 4:
            view_students()
        case 5:
            display_dashboard()

    display_edit_module_schedule(module_id)


def display_edit_module():
    print("\nSelect module:")
    for index, module_id in enumerate(trainer_info["modules"]):
        print(f"{index + 1}. { module.get(module_id)['name'] }")

    selected_index = int(input("\nEnter choice: ")) - 1
    selected_id = trainer_info["modules"][selected_index]

    print(f"\nSelected module {module.get(selected_id)['name']}")
    print("1. Edit name")
    print("2. Edit schedule")
    print("3. View module students")
    print("4. Back")

    def view_students(module_id):
        for index, student_id in enumerate(module.get(module_id)["students"]):
            print(f"{index + 1}. {student.get(student_id)['name']}")

        input("\nPress enter to continue...")
        display_edit_module()

    match int(input("\nEnter choice: ")):
        case 1:
            display_edit_module_name(selected_id)
        case 2:
            display_edit_module_schedule(selected_id)
        case 3:
            view_students(selected_id)
        case 4:
            display_dashboard()


def display_dashboard():
    print("\nTrainer Dashboard")
    print("1. Edit profile")
    print("2. Edit module info")
    print("3. View all students")
    print("4. Send feedback")
    print("5. Exit")

    match int(input("\nEnter choice: ")):
        case 1:
            display_edit_profile()
        case 2:
            display_edit_module()
        case 3:
            pass
        case 4:
            display_send_feedback()
        case 5:
            exit()


display_dashboard()
