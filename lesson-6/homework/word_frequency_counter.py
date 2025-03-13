import os
import string
from collections import Counter

# Check if "sample.txt" exists, if not, prompt the user to create it
if not os.path.exists("sample.txt"):
    print(
        "The file 'sample.txt' does not exist. Please enter a paragraph to create it:"
    )
    with open("sample.txt", "w") as file:
        file.write(input() + "\n")  # Save user input as file content

# Read file content and process words
with open("sample.txt", "r") as file:
    text = file.read().lower()  # Convert text to lowercase to ignore capitalization
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )  # Remove punctuation
    words = text.split()  # Split text into words

# Count word frequency
word_count = Counter(words)

# Get total number of words
total_words = sum(word_count.values())

# Get top 5 most common words
top_words = word_count.most_common(5)

# Display results
print(f"Total number of words: {total_words}")
print("Top 5 most common words:")
for word, count in top_words:
    print(f"{word}: {count}")

# Save results to "word_count_report.txt"
with open("word_count_report.txt", "w") as report:
    report.write(f"Total number of words: {total_words}\n")
    report.write("Top 5 most common words:\n")
    for word, count in top_words:
        report.write(f"{word}: {count}\n")

print("Word count report saved to 'word_count_report.txt'.")
