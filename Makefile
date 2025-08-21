install: #после первого клонирования установка зависимостей
	uv sync
brain-games: #запуск игры
	uv run brain-games
build:
	uv build
package-install:
	uv tool install dist/*.whl
