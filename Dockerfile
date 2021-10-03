FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install -U -r requirements.txt

ENTRYPOINT ["python"]
CMD ["src/app.py"]
