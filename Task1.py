import json
import os
from datetime import datetime

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        return tasks
    else:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def show_tasks():
    tasks = load_tasks()
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {task['date']}")
    else:
        print("Your To-Do List is empty.")

def add_task(title):
    tasks = load_tasks()
    date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_task = {"title": title, "date": date_created}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added to your To-Do List.")

def remove_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' removed from your To-Do List.")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            title = input("Enter the task title: ")
            add_task(title)
        elif choice == '3':
            index = int(input("Enter the task index to remove: "))
            remove_task(index)
        elif choice == '4':
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
