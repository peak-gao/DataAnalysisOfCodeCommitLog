from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import loadData as ld

commitLogs = ld.loadCommitLogs()
frame = DataFrame(commitLogs)

date_value_counts = frame['date'].value_counts().sort_index(level=1)

ts = pd.DataFrame(
    date_value_counts.values, index=date_value_counts.index, columns=['total'])
ts.plot(title='commit counts of each day(2016-01-01 ~ 2017-11-15)')