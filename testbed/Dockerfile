FROM phusion/baseimage

MAINTAINER lee@leeharkness.com

RUN apt-get update
RUN apt-get -y install python-pip python-dev build-essential 
RUN pip install flask ZODB 

ADD src /src

RUN mkdir -p /etc/testbed/data.db/

# @Volume /home/core/docker-containers/testbed/data.db:/etc/testbed/data.db
VOLUME ["/etc/testbed/data.db"]

EXPOSE 5020

WORKDIR /src
CMD ["python", "app.py"]

