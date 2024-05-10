FROM gcr.io/distroless/python3-debian12:nonroot

WORKDIR /hypnus

COPY --chown=nonroot:nonroot --chmod=755 hypnus .

ENV PYTHONPATH="/"
ENTRYPOINT [ "/hypnus/main.py" ]