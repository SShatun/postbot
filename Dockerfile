FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install -U -r requirements.txt

ENTRYPOINT ["python"]
CMD ["src/app.py"]
