FROM python:3.12-slim

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y \
    curl \
    && apt-get clean


RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

RUN mkdir /Ukrainian-NPPs
WORKDIR /Ukrainian-NPPs

COPY pyproject.toml poetry.lock .
RUN poetry install --no-root --only main

COPY /app /src .

CMD [ "poetry", "run", "python", "-m", "app.main"]