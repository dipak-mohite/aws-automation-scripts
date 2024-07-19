import pymysql

# RDS configuration
rds_host = 'your-rds-endpoint'
db_user = 'admin'
db_password = 'password'
db_name = 'your_database_name'

def create_connection():
    connection = pymysql.connect(
        host=rds_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    return connection

def create_table():
    connection = create_connection()
    try:
        with connection.cursor() as cursor:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS student (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                prn VARCHAR(20) UNIQUE,
                city VARCHAR(100),
                mobileno VARCHAR(15)
            )
            """
            cursor.execute(create_table_query)
            connection.commit()
            print('Table created successfully')
    finally:
        connection.close()

def insert_data(name, prn, city, mobileno):
    connection = create_connection()
    try:
        with connection.cursor() as cursor:
            insert_query = """
            INSERT INTO student (name, prn, city, mobileno)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (name, prn, city, mobileno))
            connection.commit()
            print('Data inserted successfully')
    finally:
        connection.close()

def update_data(prn, new_city, new_mobileno):
    connection = create_connection()
    try:
        with connection.cursor() as cursor:
            update_query = """
            UPDATE student
            SET city = %s, mobileno = %s
            WHERE prn = %s
            """
            cursor.execute(update_query, (new_city, new_mobileno, prn))
            connection.commit()
            print('Data updated successfully')
    finally:
        connection.close()

def delete_data(prn):
    connection = create_connection()
    try:
        with connection.cursor() as cursor:
            delete_query = """
            DELETE FROM student
            WHERE prn = %s
            """
            cursor.execute(delete_query, (prn,))
            connection.commit()
            print('Data deleted successfully')
    finally:
        connection.close()

if __name__ == "__main__":
    # Example usage
    create_table()
    insert_data('Dipak Mohite', '202202040015', 'Pune', '7620318052')
    update_data('202202040015', 'Mumbai', '9823456789')
    delete_data('202202040015')
