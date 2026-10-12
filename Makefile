init:
	uv init

install:
	uv sync

test:
	uv run pytest -v -s --headed --slowmo=500

test-coverage:
	uv run pytest -v -s -m "not flaky" --cov=steps --cov=pages --cov-report xml

lint:
	uv run ruff check --fix pages tests steps utils config.py

check: test lint

start:
	docker run --rm -d -p 5173:5173 hexletprojects/qa_auto_python_testing_kanban_board_project_ru_app
