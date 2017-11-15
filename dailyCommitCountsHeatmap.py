from pandas import DataFrame, Series
from dateutil import parser
import numpy as np
import calmap
import loadData as ld

records = ld.load()
frame = DataFrame(records)

date_value_counts = frame['date'].value_counts().sort_index(level=1)
all_days = [parser.parse(x) for x in date_value_counts.index]
events = pd.Series(date_value_counts.values, index=all_days)
calmap.calendarplot(events, cmap='YlGn')
