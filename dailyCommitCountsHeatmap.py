from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import loadData as ld
import seaborn as sns

records = ld.load()
frame = DataFrame(records)

# date_value_counts = frame.pivot()
# date_value_counts.plot(title='commit couts of each day(2016-01-01 ~ 2017-11-15)')

# ts = pd.DataFrame(date_value_counts.values, index=date_value_counts.index, columns=['total'])
# ts.plot(title='commit counts of each day(2016-01-01 ~ 2017-11-15)')

