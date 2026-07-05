def todo_app():
    tasks = []
    print("--- CodSoft Python To-Do List Application ---")

    while True:
        print("\n===== MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update/Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit Application")
        
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            if not tasks:
                print("\nYour to-do list is currently empty!")
            else:
                print("\n--- Your Tasks ---")
                for index, task in enumerate(tasks, start=1):
                    status = "✓" if task['completed'] else " "
                    print(f"{index}. [{status}] {task['title']}")
                    
        elif choice == '2':
            title = input("\nEnter the task name: ").strip()
            if title:
                tasks.append({'title': title, 'completed': False})
                print(f"Added task: '{title}'")
            else:
                print("Task name cannot be empty.")
                
        elif choice == '3':
            if not tasks:
                print("\nNo tasks to update.")
                continue
            try:
                num = int(input(f"\nEnter task number to complete (1-{len(tasks)}): "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1]['completed'] = True
                    print(f"Task '{tasks[num - 1]['title']}' marked complete!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '4':
            if not tasks:
                print("\nNo tasks to delete.")
                continue
            try:
                num = int(input(f"\nEnter task number to delete (1-{len(tasks)}): "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Deleted task: '{removed['title']}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '5':
            print("\nThank you for using the To-Do List Application! Goodbye.")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 5.")

if __name__ == "__main__":
    todo_app()