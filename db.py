from connection import get_connection


def create_table():
    try:
        conn = get_connection()

        cursor = conn.cursor()
        cursor.execute("Create table user_register(id integer auto_increment primary key, name varchar(255) not null, username varchar(255) not null, password varchar(255))")

        conn.commit()
        print("Table created successfully")
    except Exception as e:
        print(f"Error {e}")

create_table()