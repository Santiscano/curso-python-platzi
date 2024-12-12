import csv
import os
import utils
import matplotlib.pyplot as plt

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


file_path = os.path.join(os.path.dirname(__file__), 'data.csv')
data = read_csv(file_path)
country = input('Type Country => ')
result = utils.population_by_country(data, country)

if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    generate_bar_chart(labels, values)