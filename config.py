import os

IMPLEMENTATION = os.getenv("IMPLEMENTATION")
if IMPLEMENTATION:
	os.environ['APP_BASE_URL'] = f"http://{IMPLEMENTATION}.test"
else:
	os.environ['APP_BASE_URL'] = os.getenv("APP_BASE_URL", "http://localhost:5173")
LOGIN = os.getenv("LOGIN", "test")
PASSWORD = os.getenv("PASSWORD", "test")
APP_BASE_URL = os.getenv("APP_BASE_URL")
