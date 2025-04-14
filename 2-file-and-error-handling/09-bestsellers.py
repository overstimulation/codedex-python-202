import csv

with open('Bestseller.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    max_sales = 0
    best_selling_book = None

    header = next(csv_reader, None)
    if header:
        for row in csv_reader:
            current_sales = float(row[4])
            if current_sales > max_sales:
                max_sales = current_sales
                best_selling_book = row

if best_selling_book:
    with open('bestseller_info.csv', 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])
        csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])