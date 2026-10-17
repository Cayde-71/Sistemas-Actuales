FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir Flask
COPY app.py calculadora.py ./
EXPOSE 5050
CMD ["python", "-u", "app.py"]