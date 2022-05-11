import csv

with open('text.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = [raw for raw in csv_reader]

data.append(['Mike', '20', 'male'])
print(data)

with open('text.csv', 'w') as text_file:
    csv_writer = csv.writer(text_file, delimiter=',')
    for row in data:
        csv_writer.writerow(row)