FROM python:3.9.6
COPY . .
WORKDIR /tests/

RUN apt-get install -y python3.6 
RUN pip3 install -r requirements.txt

CMD ["alias python3=/usr/bin/python3.6", "python3 -m pytest tests"]
