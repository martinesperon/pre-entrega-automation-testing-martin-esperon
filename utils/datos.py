import csv

def learn_csv_login(file_path):
    data = []
    with open(".../data/data_login.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append((row['usuario'], row['password']))