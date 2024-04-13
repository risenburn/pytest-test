FROM python:3.12

COPY requirements.txt .

RUN pip install -r pytest-test/requirements.txt

COPY . .
