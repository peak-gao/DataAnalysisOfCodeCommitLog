"""
create figure of monthly commit counts
"""
from pandas import DataFrame, Series
from dateutil import parser
import numpy as np
import pandas as pd
import calmap
import loadData as ld
import calendar

commitLogs = ld.loadCommitLogs()
frame = DataFrame(commitLogs)

year_month_commit_counts = frame.groupby(['year',
                                          'month']).count()['changeset']

monthly_commit_counts_2016 = year_month_commit_counts[2016]
monthly_commit_counts_2017 = year_month_commit_counts[2017]

monthIndex = [calendar.month_abbr[x] for x in monthly_commit_counts_2016.index]

values_2016 = monthly_commit_counts_2016.values
values_2017 = monthly_commit_counts_2017.values

if (len(values_2017) < len(values_2016)):
    for x in range(len(values_2017), len(values_2016)):
        values_2017 = np.append(values_2017, np.array(0))

values = np.vstack((values_2016, values_2017))

df = pd.DataFrame(values.T, index=monthIndex, columns=[2016, 2017])
df.plot(title='Monthly commit counts')