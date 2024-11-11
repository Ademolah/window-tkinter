import mysql.connector as mc


def get_connection():
    try:
        conn = mc.connect(database="students", user="root", password="Demola321@", host="localhost")
        print("connection established...")

        return conn
    except Exception as e:
        print(f"Error: {e}")