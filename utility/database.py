import mysql.connector
from dotenv import dotenv_values

# Load database configuration
config = dotenv_values('utility/config.txt')

def fetch_customer_names():
    """
    Fetches customer names from the database.
    Returns a list of customer names.
    """
    try:
        connection = mysql.connector.connect(
            host=config['host'],
            user=config['db_user'],
            password=config['db_password'],
            database=config['database'],
            port=config['port']
        )

        cursor = connection.cursor()
        cursor.execute("SELECT first_name FROM users ORDER BY RAND() LIMIT 1")  # Update the table/column names as needed
        results = cursor.fetchall()

        # Extract names from query results
        customer_names = [row[0] for row in results]

        cursor.close()
        connection.close()

        return customer_names
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return []

def fetch_category_names():
    """
    Fetches customer names from the database.
    Returns a list of customer names.
    """
    try:
        connection = mysql.connector.connect(
            host=config['host'],
            user=config['db_user'],
            password=config['db_password'],
            database=config['database'],
            port=config['port']
        )

        cursor = connection.cursor()
        cursor.execute("SELECT name FROM categories ORDER BY RAND() LIMIT 1")  # Update the table/column names as needed
        results = cursor.fetchall()

        # Extract names from query results
        customer_names = [row[0] for row in results]

        cursor.close()
        connection.close()

        return customer_names
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return []
    
