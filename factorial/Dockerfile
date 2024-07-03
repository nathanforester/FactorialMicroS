FROM python:3.8

RUN apt update

RUN apt install python3-pip -y

RUN mkdir /opt/factorial

COPY . /opt/factorial

WORKDIR /opt/factorial

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]