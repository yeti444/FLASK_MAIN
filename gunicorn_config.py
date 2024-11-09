import os

bind = 'localhost:6000'
workers = 4

accesslog = os.path.join('log', 'access.log')
errorlog = os.path.join('log', 'error.log')

access_log_format = '%(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
