FROM gcr.io/distroless/python3-debian12:nonroot

WORKDIR /morpheus

COPY --chown=nonroot:nonroot --chmod=755 morpheus .

ENV PYTHONPATH="/"
ENTRYPOINT [ "/morpheus/main.py" ]