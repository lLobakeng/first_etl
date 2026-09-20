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
        
    return transformed_customers
    