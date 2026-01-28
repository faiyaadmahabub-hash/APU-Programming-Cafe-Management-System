import sys
from random import randint
from api import lecturer, student, module, trainer
from utils import select

lecturer_id = sys.argv[1]
data = lecturer.get(lecturer_id)


def display_edit_profile():
    print("1. Edit name")
    print("2. Edit password")
    print("3. Back")

    match int(input("\nEnter choice: ")):
        case 1:
            new_name = input("\nEnter new name: ")
            lecturer.change_name(lecturer_id, new_name)
        case 2:
            new_password = input("\nEnter new password: ")
            lecturer.change_password(lecturer_id, new_password)
        case 3:
            display_dashboard()


def display_view_requests():
    for index, request in enumerate(list(data["requests"].values())):
        print(
            f"{index + 1}. {request['sender']} {request['module_request_type']} {request['module_request_level']}"
        )

    request_id_list = list(data["requests"].keys())
    selected_index = int(input("\nEnter choice: ")) - 1
    selected_request_id = request_id_list[selected_index]
    selected_request = list(data["requests"].values())[selected_index]

    selected_request_type = selected_request["module_request_type"]
    selected_request_level = selected_request["module_request_level"]

    available_modules = module.get_filtered_modules(
        selected_request_type, selected_request_level
    )
    available_module_ids = list(available_modules.keys())

    if len(available_modules) == 0:
        print(
            f"No {selected_request_type} module with level {selected_request_level} is available!"
        )

        display_dashboard()
        return

    enrolment_month = select(
        "Enrolment month?",
        [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
    ).lower()

    chosen_module_id = available_module_ids[randint(0, len(available_module_ids) - 1)]

    student.delete_request(selected_request["sender"], selected_request_id)
    student.add_module(selected_request["sender"], chosen_module_id, enrolment_month)
    module.add_student(chosen_module_id, selected_request["sender"], enrolment_month)
    lecturer.remove_request(lecturer_id, selected_request_id)

    display_dashboard()


def display_manage_students():
    print("1. Register student")
    print("2. Delete student")
    print("3. Approve enrolment requests")
    print("4. Back")

    def register_student():
        name = input("Name: ")
        tp_number = input("TP Number: ")
        contact_number = input("Contact number: ")
        address = input("Address: ")
        module_type = select("Module type?", ["python", "java", "c"])
        module_level = select("Module level?", ["beginner", "intermediate", "advanced"])
        enrolment_month = select(
            "Enrolment month?",
            [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
            ],
        ).lower()

        modules = module.get_filtered_modules(module_type, module_level)

        student_id = student.register(
            name, tp_number, contact_number, address, lecturer_id
        )

        # for index, module_data in enumerate(list(modules.values())):
        #     print(f"{'Trainer name'} {'Module name'}")
        #     print(
        #         f"{index + 1}. {trainer.get(module_data['trainer'])['name']} {module_data['name']}"
        #     )

        # selected_module_id = list(modules.keys())[int(input("\nEnter choice: ")) - 1]
        selected_module_id = list(modules.keys())[randint(0, len(modules.keys()) - 1)]

        student.add_module(
            student_id,
            selected_module_id,
            enrolment_month,
        )
        module.add_student(selected_module_id, student_id, enrolment_month)

        print(f"Successfully registered student with id {student_id}\n")

        display_manage_students()

    def delete_profile():
        students = student.get_all()

        for index, student_data in enumerate(students):
            print(f"{index + 1}. { student_data['name'] } {student_data['tp_number']}")

        student_index = int(input("\nEnter which student to delete: ")) - 1
        selected_student_id = students[student_index]["id"]
        student.delete(selected_student_id)

        module.remove_student(selected_student_id)

        print(f"Successfully deleted student with id {selected_student_id}\n")

        display_manage_students()

    match int(input("\nEnter choice: ")):
        case 1:
            register_student()
        case 2:
            delete_profile()
        case 3:
            pass
        case 4:
            display_dashboard()


def display_dashboard():
    print("\nLecturer dashboard")
    print("1. Edit profile")
    print("2. Manage students")
    print("3. View enrollment requests")
    print("4. Exit")

    match int(input("\nEnter choice: ")):
        case 1:
            display_edit_profile()
        case 2:
            display_manage_students()
        case 3:
            display_view_requests()
        case 4:
            exit()


display_dashboard()

"""
1. manage students
    -> 1. register student
          -> 1. name?
             2. tp number?
             3. contact number?
             4. address?
             5. module type? -> python/java/c
             6. module level?
             7. choose 1 module -> lists all module w/ matching type & level
             8. enrolment month? -> selection of months
       2. delete student
       3. Approve enrolment requests
       4. back
2. edit profile
    -> 1. edit name
,       2. edit password
       3. back
"""
