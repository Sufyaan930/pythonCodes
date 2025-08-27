import os

FILENAME = "tasks.txt"

# Load tasks from file if it exists
def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            tasks = file.read().splitlines()
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n===== TO-DO LIST APP =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print(f"✅ Task '{task}' added!")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"🗑️ Task '{removed}' removed!")
    except (ValueError, IndexError):
        print("⚠️ Invalid choice. Please try again.")

def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()
