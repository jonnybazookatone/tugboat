import os
import multiprocessing
 
APP_NAME = 'tugboat'
 
bind = "0.0.0.0:80"
workers = 1
max_requests = 200
preload_app = True
chdir = os.path.dirname(__file__)
daemon = False
debug = False
errorlog = '/tmp/gunicorn-%s.error.log' % APP_NAME
accesslog = '/tmp/gunicorn-%s.access.log' % APP_NAME
pidfile = '/tmp/gunicorn-%s.pid' % APP_NAME
loglevel="info"
