import csv
def extract():
    # 1. the first thing would be to create a variable that we will eventually store our data in
    customers = []
    
    # 2. then use open() to access the actual raw file in the specified file path, 'r' means in read mode
    # the file variable represents an opened file, that automatically closes when done
    with open('data/raw/customers.csv', 'r') as file:
        
        # the actual extraction happens here, we first create a 'reader'
        reader = csv.DictReader(file)
        # then walk through the csv, one row at a time, turning each row into a dictionary and storing it in the empty list customers 
        for row in reader:
            customers.append(row)
     
    # we then return the entire collection of dictionaries
    # NOTE that the returned list of dictionaries has all its values as strings        
    return customers

