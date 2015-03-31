FROM ubuntu:latest
MAINTAINER lee@leeharkness.com

RUN apt-get update && apt-get install -y curl lsb-release supervisor python-pip python-dev
RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor
RUN locale-gen en_US en_US.UTF-8
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN echo 'root:basho' | chpasswd
RUN curl -sSL http://apt.basho.com/gpg/basho.apt.key | apt-key add --
RUN curl https://packagecloud.io/install/repositories/basho/riak/script.deb | bash
RUN apt-get install -y  riak=2.0.5-1
RUN sed -i.bak 's/127.0.0.1/0.0.0.0/' /etc/riak/riak.conf
RUN echo "ulimit -n 4096" >> /etc/default/riakA
RUN pip install flask riak
EXPOSE 8087 8098
CMD ["/usr/bin/supervisord"]
