from data import tasks

def get_all_tasks():
    return tasks

def add_task(title):

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)

    return task

def complete_task(task_id):

    for task in tasks:

        if task["id"] == task_id:
            task["completed"] = True
            return task

    return None