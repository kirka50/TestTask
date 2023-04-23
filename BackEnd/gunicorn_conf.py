# gunicorn_conf.py
from multiprocessing import cpu_count

bind = "127.0.0.1:8000"

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
#loglevel = 'debug'
#accesslog = '/home/TestTask/BackEnd/access_log'
#errorlog =  '/home/TestTask/BackEnd/error_log'
