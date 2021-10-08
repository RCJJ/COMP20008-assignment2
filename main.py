import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def analysis():
    file_path = './files/Specialist-homelessness-services-tables-2018-19.xls'
    df_1 = pd.read_excel(file_path, sheet_name='Table SHS.2')
    x = np.arange(8)
    age_list = []
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    width = 1/12
    for line in df_1.iloc[3:11].values.tolist():
        age_range = line[1]
        print(line)
        age_list.append(age_range)
        a.append(line[2])
        b.append(line[3])
        c.append(line[4])
        d.append(line[6])
        e.append(line[7])
        f.append(line[8])
    a = [x/1000 for x in a]
    print(len(a))
    c = [x/100 for x in c]
    d = [x/1000 for x in d]
    f = [x/100 for x in f]
    print(x)
    plt.bar(x-width*2.5, a, label='a', width=width, align='center')
    plt.bar(x-width*1.5, b, label='b', width=width, align='center')
    plt.bar(x-width*0.5, c, label='c', width=width, align='center')
    plt.bar(x+width*0.5, d, label='d', width=width, align='center')
    plt.bar(x+width*1.5, e, label='e', width=width, align='center')
    plt.bar(x+width*2.5, f, label='f', width=width, align='center')
    plt.xticks(x, age_list)

    print(age_list)
    plt.legend()
    plt.show()


def analysis_1():
    file_path = './files/Specialist-homelessness-services-tables-2019-20.xlsx'
    df_1 = pd.read_excel(file_path, sheet_name='Table SHS.2')
    x = np.arange(8)
    age_list = []
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    width = 1 / 12
    for line in df_1.iloc[3:11].values.tolist():
        age_range = line[1]
        print(line)
        age_list.append(age_range)
        a.append(line[2])
        b.append(line[3])
        c.append(line[4])
        d.append(line[6])
        e.append(line[7])
        f.append(line[8])
    a = [x / 1000 for x in a]
    print(len(a))
    c = [x / 100 for x in c]
    d = [x / 1000 for x in d]
    f = [x / 100 for x in f]
    print(x)
    plt.bar(x - width * 2.5, a, label='a', width=width, align='center')
    plt.bar(x - width * 1.5, b, label='b', width=width, align='center')
    plt.bar(x - width * 0.5, c, label='c', width=width, align='center')
    plt.bar(x + width * 0.5, d, label='d', width=width, align='center')
    plt.bar(x + width * 1.5, e, label='e', width=width, align='center')
    plt.bar(x + width * 2.5, f, label='f', width=width, align='center')
    plt.xticks(x, age_list)

    print(age_list)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    analysis()
    # analysis_1()

