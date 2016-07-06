FROM phusion/baseimage

RUN apt-get update
RUN apt-get install -y git python-pip python-dev nginx
RUN pip install --upgrade pip gunicorn requests

RUN echo "Starting build"
WORKDIR /app
RUN git clone https://github.com/adsabs/tugboat.git /app
RUN git checkout v1.0.3
RUN pip install -r requirements.txt

COPY resources/gunicorn.conf.py /app/gunicorn.conf.py
COPY resources/gunicorn.sh /etc/service/gunicorn/run

RUN rm /etc/nginx/sites-enabled/*
COPY resources/app.nginx.conf /etc/nginx/sites-enabled/
COPY resources/nginx.sh /etc/service/nginx/run

EXPOSE 80
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
CMD ["/sbin/my_init"]
