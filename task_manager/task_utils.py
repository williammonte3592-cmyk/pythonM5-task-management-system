from datetime import datetime
from validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):

    valid_title, title_msg = validate_task_title(title)
    if not valid_title:
        return False, title_msg
    
    valid_desc, desc_msg = validate_task_description(description)
    if not valid_desc:
        return False, desc_msg
    
    valid_date, date_msg = validate_due_date(due_date)
    if not valid_date:
        return False, date_msg

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    return True, "Task added successfully!"

def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        if tasks[index]["completed"]:
            return False, "Task is already completed"
        tasks[index]["completed"] = True
        return True, "Task marked as complete!"
    return False, "Invalid task index"

def view_pending_tasks(tasks=tasks):
    pending = []
    for task in tasks:
        if not task["completed"]:
            pending.append(task)
    return pending

def calculate_progress(tasks=tasks):
    if not tasks:
        return 0, "No tasks yet"
    
    total = len(tasks)
    completed = 0
    for task in tasks:
        if task["completed"]:
            completed += 1
    
    progress = (completed / total) * 100
    return progress, f"Progress: {progress:.1f}% ({completed}/{total} completed)"