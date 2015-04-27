FROM phusion/passenger-full

MAINTAINER lee@leeharkness.com

RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install flask ZODB 

ADD src /src


# @Volume /home/core/docker-containers/application-service/data.db:/etc/application-service/data.db
VOLUME ["/etc/application-service/data.db"]

EXPOSE 5010

WORKDIR /src
CMD ["python", "app.py"]
