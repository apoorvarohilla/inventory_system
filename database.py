import sqlite3

def init_db():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY,
        name TEXT,
        quantity INTEGER
    )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
