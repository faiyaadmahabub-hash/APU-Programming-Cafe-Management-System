import subprocess
from api import user
import os

choices = [0, 0]

roles = ["administrator", "lecturer", "trainer", "student"]

print("Enter as:")
for index, role in enumerate(roles):
    print(f"{index + 1}. {role.capitalize()}")

choices[0] = int(input("\nEnter choice: "))

print("\nAction:")
print("1. Login")
print("2. Register")

choices[1] = int(input("\nEnter choice: "))


def handle_login():
    type = roles[choices[0] - 1]

    print(f"\nLogging in as {type.capitalize()}...")
    name = input("Name: ")
    password = input("Password: ")

    status = user.check(type, name, password)

    if not status["exists"]:
        print("User does not exist!")
        return

    if status["exists"] and not status["match"]:
        print("Wrong password!")
        return

    if status["match"]:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        subprocess.run(["python", "-m", f"display.{type}", status["id"]], cwd=script_dir)


def handle_register():
    type = roles[choices[0] - 1]

    print(f"=== Register as {type} ===")
    name = input("Name: ")
    password = input("Password: ")

    if user.check(type, name, password)["exists"]:
        print("User already exists!")
        return

    user.register(type, name, password)


match choices[1]:
    case 1:
        handle_login()
    case 2:
        handle_register()
