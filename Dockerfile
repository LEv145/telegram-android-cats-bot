FROM python:3.10-alpine


WORKDIR /usr/app

RUN apk update
RUN apk add --no-cache --virtual .build-deps gcc libc-dev libffi-dev g++

RUN pip install poetry

COPY poetry.lock pyproject.toml /usr/app/
COPY src /usr/app/src

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

RUN apk del .build-deps


CMD ["poetry", "run", "telegram_android_cats_bot"]
