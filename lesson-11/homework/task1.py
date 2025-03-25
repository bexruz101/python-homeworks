import sqlite3


# Function to check if a column exists in the given table
def column_exists(cursor, table_name, column_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    return column_name in [row[1] for row in cursor.fetchall()]


# Function to create the database and the Roster table
def create_roster_database():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    # Create Roster table if it doesn't exist
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Roster (
                      Name TEXT,
                      Species TEXT,
                      Age INTEGER
                      )"""
    )

    # Insert initial data if the table is empty
    cursor.execute("SELECT COUNT(*) FROM Roster")
    if cursor.fetchone()[0] == 0:
        initial_data = [
            ("Benjamin Sisko", "Human", 40),
            ("Jadzia Dax", "Trill", 300),
            ("Kira Nerys", "Bajoran", 29),
        ]
        cursor.executemany(
            "INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", initial_data
        )

    conn.commit()
    conn.close()


# Function to update Jadzia Dax to Ezri Dax
def update_jadzia_to_ezri():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE Roster SET Name = ? WHERE Name = ?", ("Ezri Dax", "Jadzia Dax")
    )

    conn.commit()
    conn.close()


# Function to retrieve and display Bajorans' Name and Age
def query_bajorans():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = ?", ("Bajoran",))
    bajorans = cursor.fetchall()

    conn.close()
    return bajorans


# Function to delete characters older than 100 years
def delete_over_100():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Roster WHERE Age > ?", (100,))

    conn.commit()
    conn.close()


# Function to add a Rank column and update ranks
def add_rank_column():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    # Check if Rank column exists before adding
    if not column_exists(cursor, "Roster", "Rank"):
        cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT DEFAULT NULL")

    # Update ranks
    ranks = [
        ("Benjamin Sisko", "Captain"),
        ("Ezri Dax", "Lieutenant"),
        ("Kira Nerys", "Major"),
    ]
    cursor.executemany("UPDATE Roster SET Rank = ? WHERE Name = ?", ranks)

    conn.commit()
    conn.close()


# Function to retrieve all characters sorted by Age in descending order
def retrieve_sorted_by_age():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
    sorted_characters = cursor.fetchall()

    conn.close()
    return sorted_characters


# Main execution
if __name__ == "__main__":
    create_roster_database()
    update_jadzia_to_ezri()
    bajorans = query_bajorans()
    delete_over_100()
    add_rank_column()
    sorted_characters = retrieve_sorted_by_age()

    # Print sorted characters
    print("\nUpdated Roster (Sorted by Age Descending):")
    for character in sorted_characters:
        print(character)

    # Print Bajorans
    print("\nBajorans in the Roster:")
    for bajoran in bajorans:
        print(f"Name: {bajoran[0]}, Age: {bajoran[1]}")
