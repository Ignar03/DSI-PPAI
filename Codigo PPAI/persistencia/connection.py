import sqlite3

def connection():
    conn = sqlite3.connect("sismos.db")
    cursor = conn.cursor()

    return [conn, cursor]