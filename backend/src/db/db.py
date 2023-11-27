import psycopg2

database_config = {
    'host': 'localhost',
    'port': '5432',
    'database': 'passguard',
    'user': 'postgres',
    'password': 'passguard',
}

try:
    # Connect to the PostgreSQL server
    connection = psycopg2.connect(**database_config)

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Example: execute a query
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"PostgreSQL version: {version}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
