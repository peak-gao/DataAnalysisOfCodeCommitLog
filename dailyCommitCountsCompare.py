from pandas import DataFrame, Series
from dateutil import parser
import numpy as np
import pandas as pd
import calmap
import loadData as ld

records = ld.load()
frame = DataFrame(records)

year_month_commit_counts = frame.groupby(['year', 'month']).count()['changeset']

counts_2016 =  year_month_commit_counts[2016].values,
counts_2017 = year_month_commit_counts[2017].values

arr = np.array([
    year_month_commit_counts[2016].values,
    year_month_commit_counts[2017].values
])

df = pd.DataFrame(arr, columns=list('2016,2017'))

df.plot()