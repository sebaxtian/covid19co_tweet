# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

# Dependencies
import numpy as np
import pandas as pd
import requests
import unidecode
import datetime
import dateutil
import subprocess
import sys
import json
import tempfile
import os
import re

# Install missing dependencies
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

#for dirname, _, filenames in os.walk('/kaggle/input'):
#    for filename in filenames:
#        print(os.path.join(dirname, filename))

# Any results you write to the current directory are saved as output.

# %% [markdown]
# ---
# %% [markdown]
# ## Colombia Covid19 Resume
# This Notebook creates a new resume dataset, It will be used to post tweets on Twitter each time when there are new updates from datasets in [Kaggle Dataset](https://www.kaggle.com/sebaxtian/covid19co).
# 
# Dataset obtained from Kaggle after [Colombia Covid19 Pipeline](https://sebaxtian.github.io/colombia_covid_19_pipe) process run and update covid19co Dataset.
# 
# The number of new cases is increasing day by day around the world.
# 
# You can get the official dataset here: [INS - Official Report](https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr)
# %% [markdown]
# ---
# %% [markdown]
# ## Datasources

# %%
# Input data files are available in the "../kaggle/" directory.
INPUT_DIR = './'
if os.path.split(os.path.abspath('.'))[-1] == 'src':
    INPUT_DIR = '../kaggle'
# Output data files are available in the "../input/" directory.
OUTPUT_DIR = './'
if os.path.split(os.path.abspath('.'))[-1] == 'src':
    OUTPUT_DIR = '../input'

# %% [markdown]
# ---
# %% [markdown]
# ## Official Date Report

# %%
# URL Bogota Date
URL_BOGOTA_TIME = 'http://worldtimeapi.org/api/timezone/America/Bogota'
# Get Bogota Date
with requests.get(URL_BOGOTA_TIME) as bogota_time:
    bogota_time = bogota_time.json()
# Bogota Date
#print(bogota_time)
bogota_date = datetime.date.fromtimestamp(bogota_time['unixtime']).isoformat()
print('Bogota Date:', bogota_date)

try:
    # URL Date Report
    URL_DATE_REPORT = 'https://e.infogram.com/api/live/flex/efcb7f88-4bd0-4e26-a497-14ae28f6d199/a90dbc02-108d-44be-8178-b1eb6ea1fdd9?'
    # Get Official Date Report
    with requests.get(URL_DATE_REPORT) as official_date_report:
        official_date_report = official_date_report.json()
    # Official Date Report
    #print(official_date_report['data'][0][1][0])
    official_date_report = official_date_report['data'][0][1][0]
    #print(official_date_report)
    # Date Format
    date_format = official_date_report.split(' ')[4].split('-')
    # YEAR-MONTH-DAY
    official_date_report = datetime.date(int(date_format[2]), int(date_format[1]), int(date_format[0]))
except:
    official_date_report = bogota_date
# Print
print('Official Date Report:', official_date_report)

# %% [markdown]
# ---
# %% [markdown]
# ## Datasets

# %%
# Covid19 Colombia Timeline
covid19co_timeline = pd.read_csv(os.path.join(INPUT_DIR, 'covid19co_time_line.csv'))
# Show dataframe
covid19co_timeline.tail()


# %%
# Covid19 Colombia Samples Timeline
covid19co_samples_timeline = pd.read_csv(os.path.join(INPUT_DIR, 'covid19co_samples_time_line.csv'))
# Show dataframe
covid19co_samples_timeline.tail()

# %% [markdown]
# ---
# %% [markdown]
# ## Covid19 Colombia Resume

# %%
# Total Reported
# Accumulated Reported
# Total Recovered
# Accumulated Recovered
# Total Deceased
# Accumulated Deceased
# Accumulated Samples

# Data
data_resume = [official_date_report.strftime('%d/%m/%Y')] + covid19co_timeline.iloc[-1].values.tolist()[1:] + covid19co_samples_timeline.iloc[-1].values.tolist()[1:]
#print(data_resume)

# Dataframe Resume
covid19co_resume = pd.DataFrame(columns=['date', 'total_reported', 'accum_reported', 'total_recovered', 'accum_recovered', 'total_deceased', 'accum_deceased', 'accum_samples'], data=np.array([data_resume]))

# Show dataframe
covid19co_resume.head()


# %%
# Save dataframe
covid19co_resume.to_csv(os.path.join(OUTPUT_DIR, 'covid19co_resume.csv'), index=False)


# %%


