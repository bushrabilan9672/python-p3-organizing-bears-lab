#!/usr/bin/env python3

import sqlite3

def create_bears_table():
    """Creates the bears table in the database"""
    # Connect to the database (creates it if it doesn't exist)
    conn = sqlite3.connect('lib/db/bears.db')
    cursor = conn.cursor()
    
    # Create the bears table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bears (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            sex TEXT,
            color TEXT,
            temperament TEXT,
            alive BOOLEAN
        )
    ''')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_bears_table()