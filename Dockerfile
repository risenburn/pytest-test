FROM python:3.12

COPY pytest-test/requirements.txt .

RUN pip install -r requirements.txt

COPY . .
