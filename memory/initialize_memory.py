import sqlite3
def initialize_memory():

    conn = sqlite3.connect("JARVIS/memory/memory.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memories (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        category TEXT,

        key TEXT,

        value TEXT,

        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()

    conn.close()

