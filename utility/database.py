import mysql.connector
from mysql.connector import Error
from dotenv import dotenv_values

# Load database configuration
config = dotenv_values('utility/config.txt')

def execute_query(query, fetch_all=True):
    """
    Executes a query on the database and returns the results.
    
    Parameters:
        query (str): SQL query to execute.
        fetch_all (bool): Whether to fetch all results or just one.
        
    Returns:
        list: Query results as a list of tuples or an empty list on error.
    """
    try:
        # Establish a connection
        connection = mysql.connector.connect(
            host=config['host'],
            user=config['db_user'],
            password=config['db_password'],
            database=config['database'],
            port=config['port']
        )
        cursor = connection.cursor()
        cursor.execute(query)

        # Fetch results
        if fetch_all:
            results = cursor.fetchall()
        else:
            results = cursor.fetchone()
        
        cursor.close()
        connection.close()

        return results
    except Error as e:
        print(f"Database Error: {e}")
        return []

def fetch_customer_names():
    """Fetches customer names from the 'users' table."""
    query = "SELECT first_name FROM users ORDER BY RAND() LIMIT 1"
    return [row[0] for row in execute_query(query)]

def fetch_lead_names():
    """Fetches lead names from the 'marketing_leads' table."""
    query = "SELECT name FROM marketing_leads LIMIT 1"
    return [row[0] for row in execute_query(query)]

def fetch_category_names():
    """Fetches category names from the 'categories' table."""
    query = "SELECT name FROM categories ORDER BY RAND() LIMIT 1"
    return [row[0] for row in execute_query(query)]

def fetch_coupons():
    """Fetches coupon names from the 'coupons' table."""
    query = "SELECT name FROM coupons LIMIT 1"
    return [row[0] for row in execute_query(query)]

def fetch_healer_name():
    """Fetches healer names from the 'healers' table."""
    query = "SELECT healer_name FROM healers LIMIT 1"
    return [row[0] for row in execute_query(query)]
