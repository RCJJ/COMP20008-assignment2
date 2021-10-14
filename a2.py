import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange
import csv

def contacts_num():
    data = pd.read_csv(open('data/Access_to_mental_health_services.csv'), encoding = 'ISO-8859-1')
    status = data.iloc[1:4,0].values.tolist()      # indigenous status
    vic_number = data.iloc[1:4,2].values.tolist()  # vic number
    all_number = data.iloc[1:4,9].values.tolist()  # total number
    
    plt.xlabel('Indigenous status')
    plt.ylabel('Number of contacts')
    plt.xticks(arange(len(status)), status)
    plt.title('Number of Service Contacts by Indigenous Status in 2017-18', size=9)
    plt.bar(arange(len(status))-0.3,vic_number, width=0.3)
    plt.bar(arange(len(status)),all_number, width=0.3,color='r')
    plt.xticks(arange(len(status)),status)
    plt.legend(["Victoria", "National total"])
    plt.show()
    plt.savefig("contacts_num.png")
    plt.close()
    return

def contacts_rate():
    data = pd.read_csv(open('data/Access_to_mental_health_services.csv'), encoding = 'ISO-8859-1')
    status = data.iloc[[6,7,10],0].values.tolist()
    vic_rate = data.iloc[[6,7,10],2].values.tolist()
    all_rate = data.iloc[[6,7,10],9].values.tolist()
    
    plt.xlabel('Indigenous status')
    plt.ylabel('Number per 1000 population')
    plt.xticks(arange(len(status)), status)
    plt.title('Number per 1000 population for Service Contacts by Indigenous Status in 2017-18', size=9)
    plt.bar(arange(len(status))-0.3,vic_rate, width=0.3)
    plt.bar(arange(len(status)),all_rate, width=0.3,color='r')
    plt.xticks(arange(len(status)),status)
    plt.legend(["Victoria", "National total"])
    plt.show()
    plt.savefig("per_num.png")
    plt.close()
    return

def compare():
    data2 = pd.read_csv(open('data/mental health services.csv'), encoding = 'ISO-8859-1')
    
    lst1 = data2.iloc[0,10:16].values.tolist()
    line1 = pd.Series(lst1)
    lst2 = data2.iloc[1,10:16].values.tolist()
    line2 = pd.Series(lst2)
    lst3 = data2.iloc[8,10:16].values.tolist()
    line3 = pd.Series(lst3)
    lst4 = data2.iloc[9,10:16].values.tolist()
    line4 = pd.Series(lst4)
    
    x_name = []
    for i in range(3, 9):
        x_name.append('201'+str(i)+'-1'+str(i+1))
        
    plt.xticks(range(6), x_name)
    plt.plot(line1, 'b-', linewidth=2.0, label='total_indigenous')
    plt.plot(line2, 'g-', linewidth=2.0, label='total_non-indigenous')
    plt.plot(line3, 'r-', linewidth=2.0, label="VIC_indigenous")
    plt.plot(line4, 'm-', linewidth=2.0, label='VIC_non-indigenous')
    plt.xlabel('year')
    plt.ylabel('numebr per 1000')
    plt.title('Number per 1000 population of Contacts from 2013 to 2019', size=9)
    plt.legend(prop={"size": 7.5})
    plt.show()
    plt.savefig("line.png")
    plt.close()
    return 
    
if __name__ == '__main__':
    contacts_num()
    contacts_rate()
    compare()
    