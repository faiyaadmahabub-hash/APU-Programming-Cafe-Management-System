import sys
import datetime
from api import student, lecturer, module
from utils import select

id = sys.argv[1]
data = student.get(id)


def display_manage_requests():
    print("1. Send request")
    print("2. Delete request")
    print("3. Back")

    def send_request():
        module_type = select("Requested module type?", ["python", "java", "c"])
        module_level = select(
            "Requested module level?", ["beginner", "intermediate", "advanced"]
        )

        request_id, request_data = student.add_request(id, module_type, module_level)

        lecturer.add_request(data["lecturer"], request_id, request_data)

        display_manage_requests()

    def delete_request():
        for index, request in enumerate(list(data["requests"].values())):
            print(
                f"{index + 1}. {request['status']} {request['module_request_type']} {request['module_request_level']}"
            )

        selected_request_index = int(input("\nEnter choice: ")) - 1
        selected_request_id = list(data["requests"].keys())[selected_request_index]

        student.delete_request(id, selected_request_id)
        lecturer.delete_request(data["lecturer"], selected_request_id)

        display_dashboard()

    match int(input("\nEnter choice: ")):
        case 1:
            send_request()
        case 2:
            delete_request()
        case 3:
            display_dashboard()


def display_view_schedule():
    for module_info in data["modules"]:
        module_data = module.get(module_info["id"])

        if module_info["invoice"] != 0:
            print(f"\nModule name: { module_data['name']} (Unpaid)")
            print(f"You are not able to see the schedules of unpaid modules.")
            continue

        print(f"\nModule name: { module_data['name'] }")

        if len(module_data["schedule"]) == 0:
            print("No schedule for this module")
            continue

        for index, schedule in enumerate(module_data["schedule"]):
            datetime_obj = datetime.datetime.fromisoformat(schedule)
            print(
                f"{index + 1}. {datetime_obj.date().strftime('%A, %b %d %Y')} - {datetime_obj.time().strftime('%I:%M %p')}"
            )

    input("\nPress enter to continue...")
    display_dashboard()


def display_view_invoice():
    unpaid_modules = []

    for module_info in data["modules"]:
        if module_info["invoice"] != 0:
            unpaid_modules.append(module_info)

    if len(unpaid_modules) == 0:
        print("\nAll modules paid!")

        display_dashboard()
        return

    for index, module_info in enumerate(unpaid_modules):
        module_data = module.get(module_info["id"])

        print(f"{index + 1}. {module_data['name']} {module_info['invoice']}")

    selected_index = int(input("\nEnter which module to pay: ")) - 1
    student.pay_invoice(id, unpaid_modules[selected_index]["id"])

    display_dashboard()


def display_edit_profile():
    print("1. Change password")
    print("2. Change contact number")
    print("3. Change address")
    print("4. Back")

    match int(input("\nEnter choice:")):
        case 1:
            student.change_password(id, input("\nNew password: "))
            display_edit_profile()
        case 2:
            student.change_contact(id, input("\nEnter new contact number: "))
            display_edit_profile()
        case 3:
            student.change_address(id, input("\nEnter new address: "))
            display_edit_profile()
        case 4:
            display_dashboard()


def display_dashboard():
    print("\nStudent dashboard")
    print("1. Edit profile")
    print("2. View schedule")
    print("3. Manage enrollment requests")
    print("4. View invoices")
    print("5. Exit")

    match int(input("\nEnter choice: ")):
        case 1:
            display_edit_profile()
        case 2:
            display_view_schedule()
        case 3:
            display_manage_requests()
        case 4:
            display_view_invoice()
        case 5:
            exit()


display_dashboard()
