import csv


with open('data_csv.csv', 'r', encoding='utf-8') as f:
    fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
    reader = csv.DictReader(f, fields, delimiter=';')
    money_total = 0
    for row in reader:
        money_total += float(row['balance'])
    print(money_total)
    