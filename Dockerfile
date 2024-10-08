FROM python:3.10-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . .

EXPOSE  8000

CMD ["python", "main.py"]
