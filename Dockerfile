FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN apt-get update
RUN apt-get install -y git
RUN pip install -U -r requirements.txt

ENTRYPOINT ["python"]
CMD ["src/app.py"]
