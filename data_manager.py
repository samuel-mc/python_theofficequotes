import csv

def read_data():
    data = [];
    with open("./data.csv", "r+") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row);
    return data;

def parse_to_dict(header, quote):
    joined = zip(header, quote);
    parsed = { key: value for key, value in joined };
    return parsed;
