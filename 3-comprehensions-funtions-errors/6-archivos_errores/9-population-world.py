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

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

file_path = os.path.join(os.path.dirname(__file__), 'data.csv')
data = read_csv(file_path)
data = list(filter(lambda item : item['Continent'] == 'South America',data))

countries = list(map(lambda x: x['Country'], data))
percentages = list(map(lambda x: x['World Population Percentage'], data))
generate_pie_chart(countries, percentages)