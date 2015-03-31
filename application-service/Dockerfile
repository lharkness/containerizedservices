FROM phusion/passenger-full

MAINTAINER lee@leeharkness.com

RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install flask CodernityDB 

ADD src /src

EXPOSE 5010

WORKDIR /src
CMD ["python", "app.py"]
