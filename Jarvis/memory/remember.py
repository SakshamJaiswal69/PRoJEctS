def remember(category, key, value):

    conn = sqlite3.connect("memory.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM memories WHERE key=?",
        (key,)
    )

    existing = cursor.fetchone()

    if existing:

        cursor.execute(
            """
            UPDATE memories
            SET value=?
            WHERE key=?
            """,
            (value, key)
        )

    else:

        cursor.execute(
            """
            INSERT INTO memories
            (category, key, value)

            VALUES (?, ?, ?)
            """,
            (category, key, value)
        )

    conn.commit()

    conn.close()

    speak(f"I will remember that {key} is {value}")
