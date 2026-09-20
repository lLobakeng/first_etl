import random
import csv

def generate_customers():
    #set the seed for the random data
    random.seed(420)
    #creating an empty list so that we add values to it
    customers = []
    countries = ['South Africa', 'Namibia', 'Botswana', 'Zimbabwe']
    account_types = ['Basic', 'Standard','Premium']
    #we now generate the data using loops and random numbers
    
    for i in range(500):
        #each column is generated here 
        customer_id = 10001 + i
        age = random.randint(18,70)
        country = random.choice(countries)
        account_type = random.choice(account_types)
        balance = random.randint(1000,100000)
        #we then create a customer variable that we then add to our empty customers variable
        customer = {
            'customer_id':customer_id,
            'age': age,
            'country': country,
            'account_type': account_type,
            'balance': balance
            }
        
        #we then add the randomly generated date to our empty list customers
        customers.append(customer)
        
    fieldnames = ['customer_id',
              'age',
              'country',
              'account_type',
              'balance'
              ]
    
    # now we need to take the list of dictionaries and create/write this into a CSV file under our raw data


    with open('data/raw/customers.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(customers)
    
        
        
    return customers
print('Starting generator...')
generate_customers()
print('generator finished')