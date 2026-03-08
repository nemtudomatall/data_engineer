# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:08:10 2026

@author: Gabriel
"""

import pandas as pd
from sqlalchemy import create_engine
import kagglehub
from kagglehub import KaggleDatasetAdapter

file_path = "student_dropout_dataset.csv"

df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "mohamedasak/online-learning-student-dropout-dataset",
  file_path)

df.head()
data = pd.DataFrame({'one': [1.0] * 100, 'seven': [7.0] * 100})

data['average'] = (data['one'] + data['seven']) / 2


engine = create_engine('postgresql://postgres:319595@localhost:5432/postgres')
df.to_sql('students', engine, if_exists='replace')
data.to_sql('test', engine, if_exists='replace')
