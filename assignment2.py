import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

datafilepath = 'data/SEIFA.csv'

def barchart():
    data = pd.read_csv(datafilepath, encoding = 'ISO-8859-1')
    data = data.set_axis(['Quintile', '16-17', '17-18', '18-19'], axis='columns')
    data = data.set_index('Quintile')
    data['16-17'] = data['16-17'].astype(int)
    data['17-18'] = data['17-18'].astype(int)
    data['18-19'] = data['18-19'].astype(int)
    year1 = data.iloc[0:, 0].values.tolist()
    year2 = data.iloc[0:, 1].values.tolist()
    year3 = data.iloc[0:, 2].values.tolist()
    x = ["Quintile 1", "Quintile 2", "Quintile 3", "Quintile 4", "Quintile 5"]
    x_axis = np.arange(len(x))
    width = 0.2
    year1

    plt.bar(x_axis - 0.2, year1, width=width, label='16-17')
    plt.bar(x_axis, year2, width=width, label='17-18')
    plt.bar(x_axis + 0.2, year3, width=width, label='18-19')

    plt.xlabel('Quintiles')
    plt.ylabel('Number of consumers')
    plt.title('Number of Consumers over the 2016-2019 period')
    plt.legend()

    plt.xticks(x_axis + width/3, x)
    plt.show()
    plt.savefig("barchart.png")
    return

barchart()