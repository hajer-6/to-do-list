

import json
import os

SAVE_FILE = "mcqueen_tasks.json"


def load_tasks():
    """Load tasks from file if it exists, otherwise start with an empty list."""
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(SAVE_FILE, "w") as f:
        json.dump(tasks, f)


def show_menu():
    print("\n LIGHTNING MCQUEEN'S TO-DO LIST  ")
    print("Gotta get ready for the big race! Here's what's on deck:\n")
    print("1. Add a task")
    print("2. View my to-do list")
    print("3. Mark a task as done")
    print("4. Remove a task")
    print("5. Quit")


def add_task(tasks):
    description = input("Enter a new task: ").strip()
    if not description:
        print("Can't add an empty task, champ.")
        return
    tasks.append({"description": description, "done": False})
    print(f'Added to the list: "{description}"')


def view_tasks(tasks):
    if not tasks:
        print("Your track is clear, champ! No tasks yet.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "x" if task["done"] else " "
        print(f"{i}. [{status}] {task['description']}")


def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    choice = input("Which task number is done? ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(tasks)):
        print("That's not a valid task number.")
        return
    index = int(choice) - 1
    tasks[index]["done"] = True
    print(f'Ka-Chow! "{tasks[index]["description"]}" is complete!')


def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    choice = input("Which task number do you want to remove? ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(tasks)):
        print("That's not a valid task number.")
        return
    index = int(choice) - 1
    removed = tasks.pop(index)
    print(f'Removed from the list: "{removed["description"]}"')


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("\nWhat's the move, champ? ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("\nSpeed. I am speed. See you at the next pit stop!")
            break
        else:
            print("That's not on the menu, rookie. Try again.")

        save_tasks(tasks)


if __name__ == "__main__":
    main()