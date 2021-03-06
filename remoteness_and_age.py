import pandas
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

def remoteness():

    # Obtaining NOCC service users from second dataset in 2018-2019
    nocc_df = pandas.read_excel("data/nocc.xlsx", sheet_name=5, usecols=[2, 8], header=None,
                            names=["Remoteness of residence", "Number of users"])
    nocc_df = nocc_df.loc[[84, 90, 96, 102, 108]]
    nocc_df = nocc_df.reset_index(drop=True)


    # Obtaining health survey estimate data from the new dataset
    survey_df = pandas.read_excel("data/healthsurvey.xls", sheet_name=1, usecols=[0, 11], header=None,
                            names=["Remoteness of residence", "Number of individuals"])
    survey_df = survey_df.loc[[40, 41, 42]]
    survey_df = survey_df.reset_index(drop=True)


    # Making list from the NOCC dataframe
    nocc_list = []
    for i in range(len(nocc_df.index)):
        nocc_list.append([nocc_df.iloc[i][0], nocc_df.iloc[i][1]])

    # Making a second list from the survey dataframe, ensuring the headings stay consistent
    # Multiplying by 1000 to account for the raw data estimates being in '000s
    surveyed_list = []
    for i in range(len(survey_df.index)):
        surveyed_list.append([nocc_df.iloc[i][0], int(survey_df.iloc[i][1]*1000)])

    # Since the second dataframe has 3 categories, make the first one match this format
    sum = 0
    for region in nocc_list[:]:
        if (region[0] == "Outer regional" or region[0] == "Remote"):
            sum = sum + region[1]
            nocc_list.remove(region)
        elif (region[0] == "Very remote"):
            nocc_list.remove(region)
    nocc_list.append([surveyed_list[-1][0], sum])


    # Obtaining remoteness data from the census for Victoria
    vic_df = pandas.read_excel("data/remoteness-census.xls", sheet_name=3, usecols=[0, 17], header=None,
                                names=["Remoteness of residence", "Number of people"])
    vic_df = vic_df.loc[[121, 122, 123, 124]]
    vic_df = vic_df.reset_index(drop=True)


    # Creating a list with the data for easier analysis
    vic_list = []
    for i in range(len(vic_df.index)):
        vic_list.append([vic_df.iloc[i][0], int(vic_df.iloc[i][1])])

    # Obtaining remoteness data from the census for Australia
    aus_df = pandas.read_excel("data/remoteness-census.xls", sheet_name=3, usecols=[0, 17], header=None,
                                names=["Remoteness of residence", "Number of people"])
    aus_df = aus_df.loc[[159, 160, 161, 162, 163, 164]]
    aus_df = aus_df.reset_index(drop=True)

    aus_list = []
    for i in range(len(aus_df.index)):
        aus_list.append([aus_df.iloc[i][0], int(aus_df.iloc[i][1])])

    sum = aus_list[-2][1] + aus_list[-3][1] + aus_list[-4][1]

    for i in range(3):
        del aus_list[-2]

    aus_list.insert(2, ["Rest of Australia", sum])

    # Obtaining proportion of surveyed mental illness to total population categorised remoteness
    survey_prop = []
    prop = 0
    for i in range(len(surveyed_list)):
        prop = round(surveyed_list[i][1] / aus_list[i][1], 3)
        survey_prop.append([aus_list[i][0], prop])

    # Obtaining proportion of mental healthcare access to total population categorised remoteness
    access_prop = []
    prop = 0
    for i in range(len(nocc_list)):
        prop = round(nocc_list[i][1] / aus_list[i][1], 3)
        access_prop.append([aus_list[i][0], prop])

    # Done: Find total urban/regional/outer populations for all of australia
    # Done: Find proportion of that vs people with mental illness and access to mental healthcare
    # Done: Use those proportions on Victoria's raw population for different remoteness regions

    vic_labels = ["Major cities of Victoria", "Inner Regional Victoria", "Rest of Victoria"]
    vic_pop_surveyed = []
    raw_pop = 0
    for i in range(len(vic_list) - 1):
        raw_pop = int(survey_prop[i][1] * vic_list[i][1])
        vic_pop_surveyed.append([vic_labels[i], raw_pop])

    vic_pop_nocc = []
    raw_pop = 0
    for i in range(len(vic_list) - 1):
        raw_pop = int(access_prop[i][1] * vic_list[i][1])
        vic_pop_nocc.append([vic_labels[i], raw_pop])

    vic_surveyed_percents = []
    for i in range(len(vic_pop_surveyed)):
        percent = round(vic_pop_surveyed[i][1] / vic_list[i][1] * 100, 2)
        vic_surveyed_percents.append(percent)

    vic_nocc_percents = []
    for i in range(len(vic_pop_nocc)):
        percent = round(vic_pop_nocc[i][1] / vic_list[i][1] * 100, 2)
        vic_nocc_percents.append(percent)

    # Making bar chart
    vic_surveyed_percents_str = []
    for i in range(len(vic_surveyed_percents[:])):
        vic_surveyed_percents_str.append(f"{vic_surveyed_percents[i]}%")

    vic_nocc_percents_str = []
    for i in range(len(vic_nocc_percents[:])):
        vic_nocc_percents_str.append(f"{vic_nocc_percents[i]}%")

    width = 0.40
    x = np.arange(3)
    y = np.arange(8)
    vic_survey_bar = plt.bar(x - 0.2, vic_surveyed_percents, width)
    vic_nocc_bar = plt.bar(x + 0.2, vic_nocc_percents, width)
    plt.xticks(x, ["Major City", "Inner Regional", "Outer Regional"])
    plt.xlabel("Remoteness of residence", style='italic')
    plt.ylabel("Percent of population", style='italic')
    plt.legend(["Population with mental health conditions", "Population that accesses mental healthcare"],
               prop={"size": 7.75})
    plt.title("Regional access to mental healthcare in Victoria")
    #plt.bar_label(vic_nocc_bar, vic_nocc_percents_str) #does not work on older version from JupyterHub
    #plt.bar_label(vic_survey_bar, vic_surveyed_percents_str) #does not work on older version from JupyterHub
    for i in range(len(vic_surveyed_percents)):
        plt.annotate(f"{vic_nocc_percents[i]}%", xy=(i+0.2, vic_nocc_percents[i]+0.1), ha="center", va="bottom")
    plt.tight_layout()
    plt.savefig("victoria.png", dpi=300)
    plt.show()
    plt.close()

    # Setting up data for bar chart plot with normalised data (percents) for all of Australia
    surveyed_percents = []
    for i in range(len(surveyed_list)):
        percent = round(surveyed_list[i][1] / aus_list[i][1] * 100, 2)
        surveyed_percents.append(percent)

    nocc_percents = []
    for i in range(len(nocc_list)):
        percent = round(nocc_list[i][1] / aus_list[i][1] * 100, 2)
        nocc_percents.append(percent)

    # Making bar chart
    surveyed_percents_str = []
    for i in range(len(surveyed_percents[:])):
        surveyed_percents_str.append(f"{surveyed_percents[i]}%")

    nocc_percents_str = []
    for i in range(len(nocc_percents[:])):
        nocc_percents_str.append(f"{nocc_percents[i]}%")

    width = 0.40
    x = np.arange(3)
    y = np.arange(8)
    survey_bar = plt.bar(x - 0.2, surveyed_percents, width)
    nocc_bar = plt.bar(x + 0.2, nocc_percents, width)
    plt.xticks(x, ["Major City", "Inner Regional", "Outer Regional"])
    plt.xlabel("Remoteness of residence", style='italic')
    plt.ylabel("Percent of population", style='italic')
    plt.legend(["Population with mental health conditions", "Population that accesses mental healthcare"], prop={"size":7.75})
    plt.title("Regional access to mental healthcare in Australia")
    #plt.bar_label(nocc_bar, nocc_percents_str) #does not work on older version from JupyterHub
    #plt.bar_label(survey_bar, surveyed_percents_str) #does not work on older version from JupyterHub
    for i in range(len(surveyed_percents)):
        plt.annotate(f"{nocc_percents[i]}%", xy=(i+0.2, nocc_percents[i]+0.1), ha="center", va="bottom")
    plt.tight_layout()
    plt.savefig("australia.png", dpi=300)
    plt.show()
    plt.close()

    # Determining closeness of population distributions between Aus and Vic
    aus_ratios = []
    for i in range(len(aus_list) - 1):
        ratio = 0
        ratio = (round(aus_list[i][1]/aus_list[-1][1]*100, 2))
        aus_ratios.append(f"{ratio}%")

    vic_ratios = []
    for i in range(len(vic_list) - 1):
        ratio = 0
        ratio = (round(vic_list[i][1] / vic_list[-1][1] * 100, 2))
        vic_ratios.append(f"{ratio}%")

    all_ratios = []
    loc_list = ["Australia", "Victoria"]

    all_ratios.append(aus_ratios)
    all_ratios.append(vic_ratios)
    dist_df = pandas.DataFrame(all_ratios, columns=['Major Cities', 'Inner Regional', "Outer Regional"])
    dist_df.insert(0, "Location", loc_list)
    print(dist_df)
    #dfi.export(dist_df, "dist_comparison.png")

    # Finding ratio of health care conditions to access
    percent_list = []
    for i in range(len(nocc_list)):
        percent = round(nocc_list[i][1]/surveyed_list[i][1]*100, 2)
        percent_list.append([nocc_list[i][0], percent])

    # Making bar chart
    access_values = []
    for elem in nocc_list:
        access_values.append(elem[1])

    estimate_values = []
    for elem in surveyed_list:
        estimate_values.append(elem[1])

    width = 0.40
    x = np.arange(3)
    y = np.arange(8)
    annotate_list = [8.24, 9.74, 14.13]
    plt.bar(x - 0.2, estimate_values, width)
    test = plt.bar(x + 0.2, access_values, width)
    plt.xticks(x, ["Major City", "Inner Regional", "Outer Regional"])
    plt.xlabel("Remoteness of residence", style='italic')
    plt.ylabel("Population (millions)", style='italic')
    plt.legend(["Population with mental health conditions", "Population that accesses mental healthcare"])
    plt.title("Regional access to mental healthcare in Australia")
    # plt.bar_label(test, ["8.24%", "9.74%", "14.13%"])
    for i in range(len(annotate_list)):
        plt.annotate(f"{annotate_list[i]}%", xy=(i+0.2, access_values[i]+0.1), ha="center", va="bottom")
    plt.savefig("australia_raw.png", dpi=300)
    plt.show()
    plt.close()

    # Code for Raw pop bar chart vic
    vic_access_values = []
    for elem in vic_pop_nocc:
        vic_access_values.append(elem[1])

    vic_estimate_values = []
    for elem in vic_pop_surveyed:
        vic_estimate_values.append(elem[1])

    # Finding ratio of health care conditions to access in vic
    vic_percent_list = []
    for i in range(len(vic_pop_nocc)):
        percent = round(vic_pop_nocc[i][1] / vic_pop_surveyed[i][1] * 100, 2)
        vic_percent_list.append(f"{percent}%")

    width = 0.40
    x = np.arange(3)
    y = np.arange(8)
    plt.bar(x - 0.2, vic_estimate_values, width)
    test = plt.bar(x + 0.2, vic_access_values, width)
    plt.xticks(x, ["Major City", "Inner Regional", "Rest of Victoria"])
    plt.xlabel("Remoteness of residence", style='italic')
    plt.ylabel("Population", style='italic')
    plt.legend(["Population with mental health conditions", "Population that accesses mental healthcare"])
    plt.title("Regional access to mental healthcare in Victoria")
    # plt.bar_label(test, vic_percent_list)
    for i in range(len(annotate_list)):
        plt.annotate(vic_percent_list[i], xy=(i+0.2, vic_access_values[i]+0.1), ha="center", va="bottom")
    plt.tight_layout()
    plt.savefig("victoria_raw.png", dpi=300)
    plt.show()
    plt.close

def age():
    # Scatter plot: x = age, y = healthcare outcomes
    # Do all australia
    # Use histograms to compare NOCC access to age distribution in population
    # Extrapolate to VIC

    # Getting age NOCC data for age
    age_df = pandas.read_excel("data/nocc.xlsx", sheet_name=5, usecols=[2, 8], header=None,
                                names=["Age Bracket", "Consumers recieving mental healthcare"])
    age_df = age_df.loc[[6, 12, 18, 24, 30, 36, 42, 48, 54]]
    age_df = age_df.reset_index(drop=True)

    # Creating a list of age brackets for bar chart labels
    age_brackets = []
    for i in range(len(age_df.index)):
        age_brackets.append(age_df.iloc[i][0])

    # Creating NOCC bar chart to compare to census for population distribution
    age_df.plot.bar(xlabel="Age Bracket", ylabel="Population", legend=None,
                    title="Mental healthcare recipients by age")
    plt.xticks(ticks=[0, 1, 2, 3, 4, 5, 6, 7, 8], labels=age_brackets)
    plt.tight_layout()
    plt.savefig("age_bar.png", dpi=300)
    plt.show()
    plt.close()

    # Obtaining total population count for age brackets from census
    age_brackets = ["0-4", "5-9", "10-14", "15-19", "20-24","25-29","30-34","35-39","40-44","45-49","50-54","55-59","60-64","65-69","70-74","75+"]
    census_df = pandas.read_excel("data/remoteness-census.xls", sheet_name=3, usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                                  header=None, names=age_brackets)
    census_df = census_df.loc[[164]]

    # Creating census bar chart to compare to NOCC for population distribution
    census_df.plot.bar(xlabel="Age Bracket", ylabel="Population (millions)", width = 2,
                       title="Total population by age for all of Australia")
    plt.tick_params(axis='x',  which='both',  bottom=False, top=False,labelbottom=False)
    plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
    plt.tight_layout()
    plt.savefig("census_bar.png", dpi=300)
    plt.show()
    plt.close()

    # Creating scatterplot for NOCC to analyse the age to healthcare trend
    ax1 = age_df.plot.scatter(x="Age Bracket", y="Consumers recieving mental healthcare",
                              title="Scatter plot to compare age and mental healthcare recipients")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("age_scatter.png", dpi=300)
    plt.show()
    plt.close()

    # Obtaining VIC's population count for age brackets from census
    vic_census_df = pandas.read_excel("data/remoteness-census.xls", sheet_name=3,
                                  usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                                  header=None, names=age_brackets)
    vic_census_df = vic_census_df.loc[[124]]

    # Creating census bar chart for VIC to compare to the total population distribution
    vic_census_df.plot.bar(xlabel="Age Bracket", ylabel="Population", width=2,
                           title="Total population by age for Victoria")
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig("vic_census_bar.png", dpi=300)
    plt.show()
    plt.close()

    # Calculating pearson correlatio coefficient

    # List of age bin averages
    avg_list = [8.5, 21, 29.5, 39.5, 49.5, 59.5, 69.5, 79.5, 85]
    vals_list_t = age_df.values.tolist()
    vals_list = [element[1] for element in vals_list_t]
    cor, p_val = pearsonr(avg_list, vals_list)
    print(f"Pearson correlation: {cor} | p-value: {p_val}")



if __name__ == "__main__":
    remoteness()
    age()
