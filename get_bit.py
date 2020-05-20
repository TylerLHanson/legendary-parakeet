import os
import quandl
import datetime
import pandas as pd
import numpy as np

quandl.ApiConfig.api_key = os.environ.get("SECRET_KEY")

quandl.get('BITCOINWATCH/MINING', start_date='2020-05-01', end_date=str(datetime.datetime.today()).split()[0])
