from src.extract import extract
from src.transform import transform
from src.load import load

# main guard - run this file when this file is executed directly
def main():
    customers = extract()
    transformed_customers = transform(customers)
    load(transformed_customers)
    
if __name__ == '__main__':
    main()