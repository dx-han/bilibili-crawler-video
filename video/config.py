# -*- coding: utf-8 -*-
"""Store basic configuration info, including env vars, pathway, url, etc."""
import os

# database URI
SQL_HOST = os.environ.get('SQL_HOST')
SQL_USERNAME = os.environ.get('SQL_USERNAME')
SQL_PASSWORD = os.environ.get('SQL_PASSWORD')
SQL_DATABASE = os.environ.get('SQL_DATABASE')
SQL_PORT = os.environ.get('SQL_PORT')
SQL_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(SQL_USERNAME, SQL_PASSWORD, SQL_HOST, SQL_PORT, SQL_DATABASE)

# path
# os.getcwd()
PATH_DATA = '/home/ds/'

# api
CRAWLER_URL = os.environ.get('CRAWLER_URL')
START_ID = 30609529
BATCH_SIZE = 100
