import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from config import *

path = NIR_ETZION_PATH
# VALUE = 'גיל'
VALUE = 'תאריך קליטה'

def value_by_sex(value, sex='מין'):
    with open(path, newline='') as f:
        df = pd.read_csv(f)
        df = df[[sex, value]]
        # remove rows with nan values
        df.dropna(subset = [value], inplace=True)
        men_df = df.loc[df[sex] == 'ז']
        women_df = df.loc[df[sex] == 'נ']
        return df, men_df, women_df

def sort_dates(dates):
    return sorted(dates, key=lambda x: (int(str(x).split('.')[1]), int(str(x).split('.')[0])))

def get_dates_counters(df, value):
    dates = list(df[value])
    sorted_dates = sort_dates(list(set((df[value]))))
    i = 0
    date_counters = []
    for date in sorted_dates:
        counter = 0
        for index, row in df.iterrows():
            if row[value] == date:
                counter += 1
        date_counters.append(counter)
    return date_counters

def get_labels(df, value):
    if value == 'גיל':
        thresholds = [10*i for i in range(10)]
        return [str(thresh) + '-' + str(thresh + 9) for thresh in thresholds]
    if value == 'תאריך קליטה':
        return sort_dates(list(set((df[value]))))

def get_age_counters(df, value):
    ages = list(df[value])
    sorted_ages = sorted(ages)
    thresholds = [10*i for i in range(10)]
    i = 0
    ages_counters = []
    for thresh in thresholds:
        counter = 0
        while i < len(sorted_ages) and (sorted_ages[i] < thresh + 9):
            counter += 1
            i += 1
        ages_counters.append(counter)
    return ages_counters
    
def get_counters(df, value):
    if value == 'גיל':
        return get_age_counters(df, value)
    if value == 'תאריך קליטה':
        return get_dates_counters(df, value)

df, men_df, women_df = value_by_sex(value=VALUE)
labels = get_labels(df, VALUE)
men_count, women_count = get_counters(men_df, VALUE), get_counters(women_df, VALUE)

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_count, width, label='Men')
rects2 = ax.bar(x + width/2, women_count, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
age_xlabel = 'Age Groups'
date_xlabel = 'Arrival Date'


ax.set_ylabel('Count')
if VALUE == 'גיל':
    ax.set_xlabel(age_xlabel)
elif VALUE == 'תאריך קליטה':
    ax.set_xlabel(date_xlabel)


ax.set_title(HOTEL + ' patients by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()