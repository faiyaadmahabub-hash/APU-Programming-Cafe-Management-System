import sys
from api import user, trainer, module, feedback
from utils import select

id = sys.argv[1]


def display_edit_profile():
    print("1. Change name")
    print("2. Change password")
    print("3. Back")

    match int(input()):
        case 1:
            changed_name = input("Change name to: ")
            user.set("administrator", id, "name", changed_name)
        case 2:
            changed_password = input("Change password to: ")
            user.set("administrator", id, "password", changed_password)
        case 3:
            display_dashboard()


def display_register_trainer():
    name = input("Trainer name:")
    module_language = select("Module language?", ["python", "java", "c"])
    module_level = select("Module level?", ["beginner", "intermediate", "advanced"])

    trainer_id = trainer.register(name)
    module_id = module.create(
        trainer_id, module_language, module_level, f"{module_language} {module_level}"
    )

    trainer.add_module(trainer_id, module_id)

    print(f"Successfully registered trainer with id {trainer_id}!")

    display_dashboard()


def display_delete_trainer():
    # TODO add 'Select by name' too maybe
    id = input("Trainer id: ")

    isDeleted = trainer.delete(id)

    if isDeleted:
        print(f"Successfully deleted trainer with id {id}")
    else:
        print(f"Trainer with the id {id} does not exist!")

    display_dashboard()


def display_manage_trainers():
    print("1. Register trainer")
    print("2. Delete trainer")
    print("3. Edit trainer")

    match int(input()):
        case 1:
            display_register_trainer()
        case 2:
            display_delete_trainer()


def display_view_feedbacks():
    feedbacks = feedback.get_all()

    max_name_length = max(
        6, max(len(trainer.get(feedback["sender"])["name"]) for feedback in feedbacks)
    )
    max_message_length = max(7, max(len(feedback["message"]) for feedback in feedbacks))

    print(
        f"\n{'Type'.ljust(10 + 2, ' ')}{'Sender'.ljust(max_name_length + 2, ' ')}{'Message'.ljust(max_message_length + 2, ' ')}"
    )

    for current_feedback in feedbacks:
        feedback_sender, feedback_type, feedback_message = list(
            current_feedback.values()
        )
        feedback_sender = trainer.get(feedback_sender)["name"]
        feedback_message = f'"{feedback_message}"'

        print(
            f"{feedback_type.capitalize().ljust(10 + 2, ' ')}{feedback_sender.capitalize().ljust(max_name_length + 2, ' ')}{feedback_message.ljust(max_message_length + 2, ' ')}"
        )

    print("\nPress enter to continue...")
    input()
    display_dashboard()


def display_dashboard():
    print("\nAdministrator Dashboard")
    print("1. Edit profile")
    print("2. Manage trainer")
    print("3. View feedbacks")
    print("4. Exit")

    match int(input("\nEnter choice: ")):
        case 1:
            display_edit_profile()
        case 2:
            display_manage_trainers()
        case 3:
            display_view_feedbacks()
        case 4:
            exit()


display_dashboard()
