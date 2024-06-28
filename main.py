import matplotlib.pyplot
import pandas as pd

stats = pd.read_csv('https://raw.githubusercontent.com/akhil-palli/nba_stats_pd_akhilpalli/main/stats_df.csv')

print(stats)

data = stats['W']

simple_chart = matplotlib.pyplot.subplot()

simple_chart.plot(data)

matplotlib.pyplot.show()


