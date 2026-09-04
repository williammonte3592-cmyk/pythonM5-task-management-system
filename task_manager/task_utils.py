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