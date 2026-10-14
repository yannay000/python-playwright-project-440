import os

IMPLEMENTATION = os.getenv("IMPLEMENTATION")
if IMPLEMENTATION:
	os.environ["APP_BASE_URL"] = f"http://{IMPLEMENTATION}.test"

APP_BASE_URL = os.getenv("APP_BASE_URL")
if not APP_BASE_URL:
	raise RuntimeError("Переменная APP_BASE_URL не задана. Укажите APP_BASE_URL или IMPLEMENTATION.")

LOGIN = os.getenv("LOGIN", "test")
PASSWORD = os.getenv("PASSWORD", "test")
