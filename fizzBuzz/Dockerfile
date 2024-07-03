FROM python:3.8

RUN apt update

RUN apt install python3-pip -y

RUN mkdir /opt/fizzBuzz

COPY . /opt/fizzBuzz

WORKDIR /opt/fizzBuzz

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]