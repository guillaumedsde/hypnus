FROM docker.io/python:3.12-slim-bookworm

WORKDIR /hypnus

COPY --chmod=755 hypnus .

ENV PYTHONPATH="/"
ENTRYPOINT [ "/hypnus/main.py" ]