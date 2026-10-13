from secrets import randbelow


def generate_user_params() -> tuple:
    user_number = randbelow(1000000)
    email = f"test{user_number}@test.ru"
    first_name = f"first_name{user_number}"
    last_name = f"last_name{user_number}"
    return email, first_name, last_name


def generate_status_params() -> tuple:
    status_number = randbelow(1000000)
    name = f"Status Name {status_number}"
    slug = f"status_name_{status_number}"
    return name, slug


def generate_label_params() -> str:
    label_number = randbelow(1000000)
    name = f"label_name_{label_number}"
    return name


def generate_task_params() -> list:
    task_number = randbelow(1000000)
    assignee = "john@google.com"
    title = f"Task {task_number}"
    status = "Published"
    return [assignee, title, status]
