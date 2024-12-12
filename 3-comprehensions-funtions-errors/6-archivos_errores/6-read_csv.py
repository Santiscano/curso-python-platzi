import csv
import os

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

if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(__file__), 'data.csv')
    data = read_csv(file_path)
    print(data[0])