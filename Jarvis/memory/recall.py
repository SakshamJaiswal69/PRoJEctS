def recall(key):

    conn = sqlite3.connect("memory.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT value
        FROM memories
        WHERE key=?
        ORDER BY id DESC
        LIMIT 1
        """,
        (key,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:

        return result[0]

    return "I do not remember that yet."

