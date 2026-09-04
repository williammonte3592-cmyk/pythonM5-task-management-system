from datetime import datetime

def validate_task_title(title):
    """Validate task title - cannot be empty"""
    if not title or title.strip() == "":
        return False, "Title cannot be empty"
    return True, "Title is valid"

def validate_task_description(description):
    """Validate task description - cannot be empty"""
    if not description or description.strip() == "":
        return False, "Description cannot be empty"
    return True, "Description is valid"

def validate_due_date(due_date):
    """Validate due date format (YYYY-MM-DD)"""
    if not due_date or due_date.strip() == "":
        return False, "Due date cannot be empty"
    
    try:
        # Check if date is in correct format
        datetime.strptime(due_date, "%Y-%m-%d")
        return True, "Due date is valid"
    except ValueError:
        return False, "Due date must be in YYYY-MM-DD format"