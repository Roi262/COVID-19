from config import *
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

path = NIR_ETZION_PATH

def plot_counter(value):
    with open(path, newline='') as f:
        df = pd.read_csv(f)
        values = df[value]

        distincts = values.value_counts()
        sizes = list(distincts)
        labels = list(distincts.index)
        # for i in range(len(sizes)):
        #     if sizes[i] < .05 * sum(sizes):
                
        labels = [label[::-1] for label in labels]
        labels.reverse()
        print(distincts)

        # colors = ['orange', 'blue']
        # explode = (0.1, 0, 0, 0)  # explode 1st slice

        # Plot
        plt.pie(sizes, labels=labels,
        autopct='%1.1f%%', startangle=140)

    plt.axis('equal')
    plt.show()

def plot_age():
    with open(path, newline='') as f:
        df = pd.read_csv(f)
        ages = list(df['גיל'].dropna())
        sorted_ages = sorted(ages)
        # thresholds = [0]
        thresholds = [10*i for i in range(10)]
        i = 0
        ages_counters = []
        labels = []
        for thresh in thresholds:
            counter = 0
            while i < len(sorted_ages) and (sorted_ages[i] < thresh + 9):
                counter += 1
                i += 1
            ages_counters.append(counter)
            labels.append(str(thresh) + '-' + str(thresh + 9))
        
        # Plot
        x = np.arange(10)
        plt.bar(x, height=ages_counters)
        plt.xticks(x, labels)
        # plt.legend(loc="upper left")
        plt.ylabel('Number of Guests')
        plt.xlabel('Age Groups')
        plt.title("Guest Ages")
        for i in range(len(ages_counters)):
            print('Age group {}: Count {}'.format(labels[i], ages_counters[i]))


    plt.show()
    print(sum(ages_counters))


def plot_sex():
    with open(path, newline='') as f:
        df = pd.read_csv(f)
        sex = df['מין']

        male_count = list(sex).count('ז')
        female_count = list(sex).count('נ')

        labels = 'Male', 'Female'
        sizes = [male_count, female_count]
        # explode = (0.1, 0, 0, 0)  # explode 1st slice
        plt.pie(sizes, labels=labels,
        autopct='%1.1f%%', startangle=140)

    plt.axis('equal')
    plt.show()

# plot_sex()
# plot_age()
# plot_counter('עיר מגורים')
plot_counter('קופת חולים')