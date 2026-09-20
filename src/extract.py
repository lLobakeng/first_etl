import csv
def extract():
    # open customers.csv
    customers = []
    with open('data/raw/customers.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers.append(row)
            
    return customers

    # read the CSV
    #return the data