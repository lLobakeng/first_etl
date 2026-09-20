import csv

def load(customers):
    fieldnames = ['customer_id',
                  'age',
                  'country',
                  'account_type',
                  'balance'
                  ]
    
    with open('data/processed/customers.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(customers)