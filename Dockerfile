FROM ubuntu:latest
MAINTAINER Danilo Nunes "nunesdanilo@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential cmake
RUN apt-get install -y libboost-all-dev
RUN apt-get install -y libcv2.4 python-opencv
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
