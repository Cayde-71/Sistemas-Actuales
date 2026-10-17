FROM ubuntu:latest
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl python3 python3-flask \
    && rm -rf /var/lib/apt/lists/*
CMD ["sh", "-c", "exec sleep infinity"]