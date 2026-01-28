def select(message, items):
    print(message)

    for index, item in enumerate(items):
        print(f"{index + 1}. {item}")

    while True:
        try:
            choice = int(input("\nEnter choice: ")) - 1
            if 0 <= choice < len(items):
                return items[choice]
            else:
                print(f"Invalid choice! Please enter a number between 1 and {len(items)}.")
        except ValueError:
            print("Invalid input! Please enter a number.")
