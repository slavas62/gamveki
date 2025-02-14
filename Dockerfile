FROM nginx:1.25.5
MAINTAINER slavas62@gmail.com

RUN apt-get update && apt-get install -y \
  supervisor \
  curl \
  git \
  gcc \
  g++ \
  python-dev \
  python-virtualenv \
  libgdal-dev \
  libpq-dev \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


ENV work_dir /app

WORKDIR ${work_dir}

ADD . .

RUN virtualenv /env

RUN cp ./docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf && \
    cp ./docker/nginx.conf /etc/nginx/conf.d/default.conf && \
    CPLUS_INCLUDE_PATH=/usr/include/gdal C_INCLUDE_PATH=/usr/include/gdal \
    /env/bin/pip install -r requirements.txt

RUN /env/bin/python /app/manage.py collectstatic --noinput

RUN mkdir /data

VOLUME /data

EXPOSE 80

# set default locale for python
ENV LANG C.UTF-8 

CMD ./docker/docker_start.sh