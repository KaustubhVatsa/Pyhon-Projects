import os

HISTORY_FILE = "History.txt"

# Create file if not exists
if not os.path.exists(HISTORY_FILE):
    open(HISTORY_FILE, "w").close()


# Display History
def display_history():
    with open(HISTORY_FILE, "r") as file:
        lines = file.readlines()
        if not lines:
            print("No History Found")
        else:
            for line in reversed(lines):
                print(line.strip())


# Clear History
def clear_history():
    open(HISTORY_FILE, "w").close()
    print("History cleared successfully!")


# Bring Last Result
def bring_last_result():
    with open(HISTORY_FILE, "r") as file:
        lines = file.readlines()
        if not lines:
            print("No History Found")
        else:
            print("Last result:", lines[-1].strip())


# Add entry to history
def add_to_history(expression, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{expression} = {result}\n")


# Calculate expression safely
def calculate_result(expression):
    try:
        result = eval(expression)
        return result
    except Exception:
        return "Error: Invalid expression"


# -----------------------
# Main Program
# -----------------------
while True:
    print("\nMenu:")
    print("1. Calculate Expression")
    print("2. Show History")
    print("3. Clear History")
    print("4. Bring Last Result")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        expression = input("Enter an expression: ")
        result = calculate_result(expression)
        print("Result:", result)

        if "Error" not in str(result):
            add_to_history(expression, result)

    elif choice == "2":
        display_history()

    elif choice == "3":
        clear_history()

    elif choice == "4":
        bring_last_result()

    elif choice == "5":
        break

    else:
        print("Invalid choice, try again!")
