from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

def main():
    while True:
        print("\n--- Task Management System ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            print("\n--- Add New Task ---")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            
            success, message = add_task(title, description, due_date)
            print(message)

        elif choice == "2":
            pending = view_pending_tasks()
            if not pending:
                print("No pending tasks.")
            else:
                print("\nPending Tasks:")
                for i, task in enumerate(pending):
                    print(f"{i+1}. {task['title']} - Due: {task['due_date']}")
                
                try:
                    task_num = int(input("Enter task number to complete: ")) - 1
                    if 0 <= task_num < len(pending):
                        success, message = mark_task_as_complete(task_num)
                        print(message)
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        