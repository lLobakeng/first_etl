import csv

def load(customers):
    fieldnames = ['customer_id',
                  'age',
                  'country',
                  'account_type',
                  'balance', 
                  'age_group'
                  ]
    # we take the final data and create a new file in the path specified
    # we are also essentially taking the list of dictionaries and converting them to a CSV file
    with open('data/processed/customers.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # this ensure that the CSV has the column headers 
        writer.writeheader()
        # writes the dictionaries underneath the header
        writer.writerows(customers)