install: #после первого клонирования установка зависимостей
	uv sync
brain-games: #запуск игры
	uv run brain-games
brain-even:
	uv run brain-even
build:
	uv build
package-install:
	uv tool install dist/*.whl
write-text:
	nano brain_games/scripts/brain_games.py

lint:
	uv run ruff check brain_games
