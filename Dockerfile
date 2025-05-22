# Используем официальный образ Python
FROM python:3.13-slim-bookworm

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем poetry.lock и pyproject.toml для установки зависимостей
COPY pyproject.toml poetry.lock /app/

# Устанавливаем Poetry
RUN pip install poetry==1.8.5

# Устанавливаем зависимости с Poetry
RUN poetry install --no-root --no-dev

# Копируем весь остальной код приложения в контейнер
# Включая bot.py и папку images
COPY . /app

# Команда для запуска вашего бота
CMD ["poetry", "run", "python", "bot.py"]