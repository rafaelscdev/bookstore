FROM python:3.12.1-slim as python-base

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DEFAULT_TIMEOUT=100
ENV PIP_DISABLE_PIP_VERSION_CHECK=on

ENV POETRY_VERSION=1.7.0
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1

ENV VIRTUAL_ENV_PATH="/opt/pysetup/.venv"
ENV PYSETUP_PATH="/opt/pysetup"

ENV PATH="$POETRY_HOME/bin:$VIRTUAL_ENV_PATH/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends curl build-essential

RUN curl -sSL https://install.python-poetry.org | python

RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./
COPY README.md ./

RUN poetry install --no-dev

WORKDIR /app
COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]