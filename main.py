import logging

from src.extract import extract
from src.transform import transform
from src.load import load

# we can create our logger object

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    filename='etl.log',
                    format='%(asctime)s %(levelname)s %(name)s %(message)s'
                    )

# main guard - run this file when this file is executed directly

def main():
    
    logger.info('Starting ETL pipeline')
    
    customers = extract()
    transformed_customers = transform(customers)
    load(transformed_customers)
    
    
if __name__ == '__main__':
    main()