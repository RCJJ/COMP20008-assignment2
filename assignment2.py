import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

datafilepath = 'data/SEIFA.csv'
datafilepath2 = 'data/Population per SEIFA Quintile.csv'
datafilepath3 = 'data/Vic Pop SEIFA dist.csv'
datafilepath4 = 'data/MHContacts per SEIFA.csv'
datafilepath5 = 'data/Age.csv'
datafilepath6 = 'data/IndigenousConsumers.csv'
datafilepath7 = 'data/IndigenousPop.csv'
datafilepath8 = 'data/IndigenousConsumersPercent.csv'

def casesperquint():
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
    plt.close()
    return

def seifapop():
    data = pd.read_csv(datafilepath2, encoding = 'ISO-8859-1')
    data = data.set_axis(['Quintile', 'Population'], axis='columns')
    data = data.set_index('Quintile')
    data['Population'] = data['Population'].astype(int)
    pop = data.iloc[0:,0].values.tolist()
    x = ["Quintile 1", "Quintile 2", "Quintile 3", "Quintile 4", "Quintile 5"]
    x_axis = np.arange(len(x))
    plt.bar(x_axis, pop)
    plt.xlabel('Quintiles')
    plt.ylabel('Population in millions')
    plt.xticks(x_axis, x)
    plt.title('Number of people living in each SEIFA quintile')
    plt.show()
    plt.savefig("Pop in SEIFA quint")
    plt.close()
    return

def seifapopvic():
    data = pd.read_csv(datafilepath3, encoding = 'ISO-8859-1')
    data = data.set_axis(['Quintile', 'Population'], axis='columns')
    data = data.set_index('Quintile')
    data['Population'] = data['Population'].astype(int)
    pop = data.iloc[0:,0].values.tolist()
    x = ["Quintile 1", "Quintile 2", "Quintile 3", "Quintile 4", "Quintile 5"]
    x_axis = np.arange(len(x))
    plt.bar(x_axis, pop)
    plt.xlabel('Quintiles')
    plt.ylabel('Population in millions')
    plt.xticks(x_axis, x)
    plt.title('Victoria Population living in each SEIFA quintile')
    plt.show()
    plt.savefig("Vic Pop in SEIFA quint")
    plt.close()
    return

def seifaviccon():
    data = pd.read_csv(datafilepath4, encoding = 'ISO-8859-1')
    data = data.set_axis(['Quintile', 'Service Contacts'], axis='columns')
    data = data.set_index('Quintile')
    data['Service Contacts'] = data['Service Contacts'].astype(int)
    con = data.iloc[0:, 0].values.tolist()
    x = ["Quintile 1", "Quintile 2", "Quintile 3", "Quintile 4", "Quintile 5"]
    x_axis = np.arange(len(x))
    plt.bar(x_axis, con)
    plt.xlabel('Quintiles')
    plt.ylabel('Number of Service Contacts')
    plt.xticks(x_axis, x)
    plt.title('Victoria Service Contacts per SEIFA quintile')
    plt.show
    plt.savefig("Vic SerCon per SEIFA quint")
    plt.close()
    return

def age():
    data = pd.read_csv(datafilepath5, encoding = 'ISO-8859-1')
    data = data.set_axis(['Age', '14-15', '15-16', '16-17', '17-18', '18-19', 'non'], axis='columns')
    data = data.set_index('Age')
    data = data.iloc[0:, 0:5]
    data['14-15'] = data['14-15'].astype(int)
    data['15-16'] = data['15-16'].astype(int)
    data['16-17'] = data['16-17'].astype(int)
    data['17-18'] = data['17-18'].astype(int)
    data['18-19'] = data['18-19'].astype(int)
    year1 = data.iloc[0:, 0].values.tolist()
    year2 = data.iloc[0:, 1].values.tolist()
    year3 = data.iloc[0:, 2].values.tolist()
    year4 = data.iloc[0:, 3].values.tolist()
    year5 = data.iloc[0:, 4].values.tolist()
    x = ["Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65-74", "75-84", "Over 85"]
    x_axis = np.arange(len(x))
    width = 0.1
    plt.figure(figsize=(8,3))
    plt.bar(x_axis-0.2, year1, width=width, label='14-15')
    plt.bar(x_axis-0.1, year2, width=width, label='15-16')
    plt.bar(x_axis, year3, width=width, label='16-17')
    plt.bar(x_axis+0.1, year4, width=width, label='17-18')
    plt.bar(x_axis+0.2, year5, width=width, label='18-19')
    plt.xlabel('Age range')
    plt.ylabel('Number of consumers')
    plt.title('Number of Consumers in each age range over the 2014-2019 period')
    plt.legend()

    plt.xticks(x_axis + width/5, x)
    plt.show()
    plt.savefig("age.png")
    plt.close()
    return

def indigpercent():
    data = pd.read_csv(datafilepath8, encoding = 'ISO-8859-1')
    data = data.set_axis(['Indigenous Status', '16-17', '17-18', '18-19'], axis='columns')
    data = data.set_index('Indigenous Status')
    data['16-17'] = data['16-17'].astype(float)
    data['17-18'] = data['17-18'].astype(float)
    data['18-19'] = data['18-19'].astype(float)
    year1 = data.iloc[0:, 0].values.tolist()
    year2 = data.iloc[0:, 1].values.tolist()
    year3 = data.iloc[0:, 2].values.tolist()
    x = ['Non-Indigenous Australians', 'Indigenous Australians']
    x_axis = np.arange(len(x))
    width = 0.2
    plt.bar(x_axis - 0.2, year1, width=width, label='16-17')
    plt.bar(x_axis, year2, width=width, label='17-18')
    plt.bar(x_axis + 0.2, year3, width=width, label='18-19')
    plt.xlabel('Indigenous Status')
    plt.ylabel('Percentage of Population')
    plt.title('Percent of Indigenous vs Non-Indigenous accesing mental healthcare')
    plt.legend()

    plt.xticks(x_axis + width/10, x)
    plt.show()
    plt.savefig("indigenouscon.png")
    plt.close()
    return

casesperquint()
seifapop()
seifapopvic()
seifaviccon()
indigpercent()