def categorize_age(customers):
    for customer in customers:
        if customer['age'] <= 30:
            customer['age_group'] = 'Young Adult'
            
        elif customer['age'] <= 50:
            customer['age_group'] = 'Adult'
        
        else:
            customer['age_group'] = 'Mature'
            
    return customers

country_codes = {
    'South Africa': 'ZA',
    'Namibia': 'NA',
    'Botswana': 'BW',
    'Zimbabwe': 'ZW'
}

def standardize_countries(customers):
    for customer in customers:
        customer['country'] = country_codes[customer['country']]
        
    return customers

def validate_customers(customers):
    valid_customers= []
    for customer in customers:
        if customer['age'] >= 18 and customer['age'] <= 70 and customer['balance'] >= 0 and customer['account_type'] in ['Basic', 'Standard', 'Premium']:
            valid_customers.append(customer)
    
    return valid_customers 



def transform(customers):
# we create a new list instead of modifying the extracted list directly
    transformed_customers = []
    
    # we now create a loop to transform the data, ie turn the strings in customer_id, balance and age
    
    for customer in customers:
        customer['customer_id'] = int(customer['customer_id'])
        customer['age'] = int(customer['age'])
        customer['balance'] = int(customer['balance'])
        
        # we then add the uptdated/transformed data to the empty list, transformed_customers
        transformed_customers.append(customer)
    
    transformed_customers = categorize_age(transformed_customers)
    transformed_customers = standardize_countries(transformed_customers) 
    transformed_customers = validate_customers(transformed_customers)
    
    return transformed_customers
       



        
    