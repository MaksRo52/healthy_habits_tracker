# Python и Poetry идеально сочетаются.
FROM python:3.8 as builder
WORKDIR /app
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev # Установка без зависимостей для разработки

# Финальный этап для Python, без Poetry.
FROM python:3.8-slim
WORKDIR /app
COPY --from=builder /app ./