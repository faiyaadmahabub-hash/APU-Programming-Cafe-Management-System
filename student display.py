from student import changePassword, changeContact, request, show_request_status, get, delete_requests
import sys


id = sys.argv[1]
student = get(id)


def edit_profile():
    print("1. Change password")
    print("2. Change contact number")
    print("3. Exit")
    match int(input("Enter choice: ")):
        case 1:
            new_password = input("New Password: ")
            confirm_password = input("Confirm Password: ")
            while len(new_password) < 6:
                print(red("Enter a longer password"))
                new_password = input("Password: ")
                confirm_password = input("Confirm your password: ")
            while new_password != confirm_password:
                print(red("Your does not match"))
                new_password = input("Enter your password: ")
                confirm_password = input("Confirm your password: ")
            changePassword(id, new_password)
        case 2:
            new_contact_num = input("New number: ")
            changeContact(id, new_contact_num)
        case 3:
            main_display()


def view_schedule():
    pass


def manage_requests():
    print("1. Send request: ")
    print("2. Show all request status")
    print("3. Delete request")
    print("exit")

    match int(input("Enter choice: ")):
        case 1:
            module = select("Requested module type?", ["Python", "Java", "c"])
            level = select("Requested module level?", ["Beginner", "Intermediate", "Advanced"])
            request(id, module, level)
        case 2:
            show_request_status(id)
        case 3:
            show_request_status(id)
            selected_index = int(input("Enter choice: "))-1
            selected_request_id = list(student["requests"].keys())[selected_index]
            delete_requests(id, selected_request_id)
            if pending == False:
                print(green("Your request has already been Accepted you cannot delete in now"))
                manage_requests()
        case 4:
            main_display()


def view_invoices():
    pass


def main_display():
    print("\nStudent Dashboard:")
    print("1. Edit profile")
    print("2. View schedule")
    print("3. Manage enrollment requests")
    print("4. View invoices")
    print("5. Exit")

    match int(input("Enter choice: ")):
        case 1:
            edit_profile()
        case 2:
            view_schedule()
        case 3:
            manage_requests()
        case 4:
            view_invoices()
        case 5:
            exit()


def green(text):
    return f"\033[92m{text}\033[0m"

def red(text):
    return f"\033[0;31m{text}\033[0m"


def select(message, items):
    print(message)

    for index, item in enumerate(items):
        print(f"{index + 1}. {item}")

    return items[int(input("\nEnter choice: ")) - 1]

