# todo.py

FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks in your list.")
    else:
        print("\n📋 Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        print()

def add_task(tasks):
    task = input("➕ Enter the task to add: ")
    tasks.append(task)
    print("✔️ Task added successfully!")

def remove_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            num = int(input("❌ Enter the task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"🗑️ Removed: '{removed}'")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("❗ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("👉 Choose an option (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose 1 to 4.")

if __name__ == "__main__":
    main()
