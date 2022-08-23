FROM python:3.9.6
COPY . .
WORKDIR /tests/

RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["python3 -m pytest tests"]
