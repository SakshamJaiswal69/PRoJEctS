
import sqlite3
def get_all_memories():

    conn = sqlite3.connect("memory.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT key, value FROM memories
    ORDER BY id DESC
    LIMIT 20
    """)

    memories = cursor.fetchall()

    conn.close()

    memory_text = ""

    for key, value in memories:
        memory_text += f"{key}: {value}\n"

    return memory_text
