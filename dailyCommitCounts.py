"""
create figure of daily commit counts
"""
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import loadData as ld

commitLogs = ld.loadCommitLogs()
frame = DataFrame(commitLogs)

date_value_counts = frame['date'].value_counts()

firtItem = date_value_counts.head(1)
print 'Maximum is {0} from date {1}, Average is {2}'.format(
    firtItem.values[0], firtItem.index[0], date_value_counts.mean())

date_value_counts = date_value_counts.sort_index(level=1)

ts = pd.DataFrame(
    date_value_counts.values, index=date_value_counts.index, columns=['total'])
ts.plot(title='Daily Commit counts(from 2016-01-01 to 2017-11-15)')