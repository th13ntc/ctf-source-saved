# docker build -t battle . && docker run -d -p 8080:80 battle

FROM php:7.4-apache

RUN rm -rf /var/www/html/
COPY * /var/www/html/
RUN mkdir /var/www/html/icons && \
    mv default.png /var/www/html/icons && \
    chmod 777 -R /var/www/html/icons

###
###
###

EXPOSE 80
CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]