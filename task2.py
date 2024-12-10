'''
Problem 2: "Library Book Borrowing Analysis"
Description:
You have a record of books borrowed from a library for a month. Each record includes the book title and the number of days  of it was borrowed. Your task is to write a program that performs the following:
Accepts a list of borrowed books wirrowed th the format: "Book Title - Days Borrowed".
Calculates the most and least borrowed book based on the number of days.
Calculates the average number of days books were borrowed.
Finds the unique titles of all borrowed books.
Sorts the books by the number of days borrowed in descending order.

'''


print("Enter borrowed books in the format 'Book Title - Days Borrowed', separated by commas:")
records = input()

# dictionary { key : value}
borrowed_books = {}
entries = records.split(",")  

for entry in entries:
    title, days = entry.strip().split(" - ")   
    days = int(days)  

    if title in borrowed_books:
        borrowed_books[title] += days 
    else:
        borrowed_books[title] = days  


most_borrowed = max(borrowed_books, key=borrowed_books.get)  
least_borrowed = min(borrowed_books, key=borrowed_books.get)  
average_days = sum(borrowed_books.values()) / len(borrowed_books)  
unique_titles = set(borrowed_books.keys())  
sorted_books = sorted(borrowed_books.items(), key=lambda x: x[1], reverse=True)  # [(x0,x1),(x0,x1)] 


print("Most Borrowed Book:", most_borrowed)
print("Least Borrowed Book:", least_borrowed)
print("Average Borrowing Time:", round(average_days, 2))
print("Unique Titles:", unique_titles)
print("Books Sorted by Borrowing Duration (Descending):")
for book, days in sorted_books:
    print(f"{book}: {days} days")
