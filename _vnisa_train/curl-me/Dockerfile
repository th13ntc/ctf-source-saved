FROM ubuntu:18.04

# Package
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y nginx php-fpm php-curl gcc

# Config
COPY conf/nginx.server.conf /etc/nginx/sites-enabled/default
COPY conf/php-fpm.conf /etc/php/7.2/fpm/php-fpm.conf

# Document
COPY html/* /var/www/html/

# Flag
COPY flag/* /
RUN gcc -o /getflag /getflag.c
RUN chmod 644 /flag1 && chmod 600 /flag2 && chmod +xs /getflag

# Dont blink
RUN chown -R root:adm /var/log/nginx

# Entry
COPY entrypoint /entrypoint
RUN chmod +x /entrypoint

CMD /entrypoint