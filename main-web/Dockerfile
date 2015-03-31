#
# https://github.com/dockerfile/nginx
#

# Pull base image.
FROM dockerfile/ubuntu

# Install Nginx.
RUN \
  add-apt-repository -y ppa:nginx/stable && \
  apt-get update && \
  apt-get install -y nginx && \
  rm -rf /var/lib/apt/lists/* && \
  echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
  chown -R www-data:www-data /var/lib/nginx

# Define mountable directories.
VOLUME ["/etc/nginx/sites-enabled","/etc/nginx", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx", "/var/www/html"]

# copy our content
COPY src /var/www/html

# Define working directory.
WORKDIR /etc/nginx

# create logs directory
RUN mkdir -p /usr/share/nginx/logs/

#copy our configuration
COPY default /etc/nginx/sites-enabled/

# Define default command.
CMD ["nginx"]

# Expose ports.
EXPOSE 80 442
