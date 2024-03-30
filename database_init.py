import sqlite3
from sqlite3 import Error
import pandas as pd

def db_initialize():
    conn = None
    try:
        # Create connection    
        conn = sqlite3.connect("air-selangor-hackathon.db")
        cursor = conn.cursor()
        
        # Build / Create Tables
        cursor.execute("""CREATE TABLE IF NOT EXISTS location (
                            location_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            location_name TEXT
                        )""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS meter_info (
                            serial_num TEXT PRIMARY KEY,
                            location_id INTEGER,
                            meter_type TEXT,
                            manufacturer TEXT,
                            model TEXT,
                            manufactured_year TEXT, -- You can store year as TEXT
                            meter_size INTEGER,
                            warranty_info TEXT,
                            FOREIGN KEY (location_id) REFERENCES location(location_id)
                        )""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS lab_tests (
                            lab_test_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            serial_num TEXT,
                            date_tested TEXT, -- Use TEXT for dates
                            date_physical_check TEXT,
                            date_received TEXT,
                            category TEXT,
                            defect TEXT,
                            results TEXT CHECK(results IN ('FAIL', 'PASS')),
                            FOREIGN KEY (serial_num) REFERENCES meter_info(serial_num)
                        )""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS meter_movement (
                            movement_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            move_from TEXT,
                            move_to TEXT,
                            serial_num TEXT,
                            purpose TEXT,
                            timestamp TEXT,
                            FOREIGN KEY (serial_num) REFERENCES meter_info(serial_num)
                        )""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS installation (
                            installation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            serial_num TEXT,
                            location_id INTEGER,
                            installation_date TEXT,
                            FOREIGN KEY (serial_num) REFERENCES meter_info(serial_num),
                            FOREIGN KEY (location_id) REFERENCES location(location_id)
                        )""")

        # Inserting data
        # Load data from CSV into a DataFrame
        meter_info = pd.read_csv('.\example_dataset\TB_ meter_info.csv')
        location = pd.read_csv('.\example_dataset\TB_ location.csv')
        lab_tests = pd.read_csv('.\example_dataset\TB_ lab_result.csv')
        installation = pd.read_csv('.\example_dataset\TB_ installation.csv')
        meter_movement = pd.read_csv('.\example_dataset\TB_ meter_movement.csv')
    
        # Insert data into the SQLite table
        meter_info.to_sql('meter_info', conn, if_exists='append', index=False)
        location.to_sql('location', conn, if_exists='append', index=False)
        lab_tests.to_sql('lab_tests', conn, if_exists='append', index=False)
        installation.to_sql('installation', conn, if_exists='append', index=False)
        meter_movement.to_sql('meter_movement', conn, if_exists='append', index=False)
        
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

db_initialize()
