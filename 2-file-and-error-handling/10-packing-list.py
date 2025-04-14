import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open('packing_list.csv') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
except:
    if FileNotFoundError:
        print('Packing list file not found. Creating a new one.')
        with open('packaging_list.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)