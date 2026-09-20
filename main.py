from src.extract import extract
from src.transform import transform
from src.load import load

customers = extract()

transformed_customers = transform(customers)

load(transformed_customers)