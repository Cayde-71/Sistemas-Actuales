FROM ubuntu:latest
COPY script.sh ./
RUN apt-get update && apt-get install -y netcat-openbsd
CMD ["sh", "-c", "sh ./script.sh; exec sleep infinity"]