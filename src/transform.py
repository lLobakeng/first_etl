def categorize_age(customers):
    for customer in customers:
        if customer['age'] <= 30:
            customer['age_group'] = 'Young Adult'
            
        elif customer['age'] <= 50:
            customer['age_group'] = 'Adult'
        
        else:
            customer['age_group'] = 'Mature'
            
    return customers



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
        
    return transformed_customers



        
    