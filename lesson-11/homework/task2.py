import sqlite3


# Function to check if a column exists in the given table
def column_exists(cursor, table_name, column_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    return column_name in [row[1] for row in cursor.fetchall()]


# Function to create the database and the Books table
def create_library_database():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Create Books table if it doesn't exist
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Books (
                      Title TEXT,
                      Author TEXT,
                      Year_Published INTEGER,
                      Genre TEXT
                      )"""
    )

    # Insert initial data if the table is empty
    cursor.execute("SELECT COUNT(*) FROM Books")
    if cursor.fetchone()[0] == 0:
        initial_data = [
            ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
            ("1984", "George Orwell", 1949, "Dystopian"),
            ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic"),
        ]
        cursor.executemany(
            "INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)",
            initial_data,
        )

    conn.commit()
    conn.close()


# Function to update the Year_Published of 1984 to 1950
def update_year_of_1984():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE Books SET Year_Published = ? WHERE Title = ?", (1950, "1984")
    )

    conn.commit()
    conn.close()


# Function to retrieve and display all Dystopian books
def query_dystopian_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT Title, Author FROM Books WHERE Genre = ?", ("Dystopian",))
    dystopian_books = cursor.fetchall()

    conn.close()
    return dystopian_books


# Function to delete books published before 1950
def delete_old_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Books WHERE Year_Published < ?", (1950,))

    conn.commit()
    conn.close()


# Function to add a Rating column and update ratings
def add_rating_column():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Check if Rating column exists before adding
    if not column_exists(cursor, "Books", "Rating"):
        cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL DEFAULT NULL")

    # Update ratings
    ratings = [("To Kill a Mockingbird", 4.8), ("1984", 4.7), ("The Great Gatsby", 4.5)]
    cursor.executemany("UPDATE Books SET Rating = ? WHERE Title = ?", ratings)

    conn.commit()
    conn.close()


# Function to retrieve all books sorted by Year_Published in ascending order
def retrieve_sorted_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
    sorted_books = cursor.fetchall()

    conn.close()
    return sorted_books


# Main execution
if __name__ == "__main__":
    create_library_database()
    update_year_of_1984()
    dystopian_books = query_dystopian_books()
    delete_old_books()
    add_rating_column()
    sorted_books = retrieve_sorted_books()

    # Print sorted books
    print("\nUpdated Library (Sorted by Year Published Ascending):")
    for book in sorted_books:
        print(book)

    # Print Dystopian books
    print("\nDystopian Books in the Library:")
    for book in dystopian_books:
        print(f"Title: {book[0]}, Author: {book[1]}")
