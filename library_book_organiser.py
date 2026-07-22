

books = [
    "Harry Potter",
    "Diary of a Wimpy Kid",
    "Geronimo Stilton",
    "Roald Dahl",
    "Percy Jackson",
    "Dog Man"
]

print("Books in the library:", books)

print("Number of books:", len(books))


books.append(input("Enter a new book name: "))
print("Updated book list:", books)

books.remove(input("Enter the name of the book to remove: "))
print("Updated book list:", books)

books.sort()
print("Sorted books:", books)


books.reverse()
print("Reversed books:", books)

print("First book:", books[0])
print("Second book:", books[1])
print("Last book:", books[-1])


print("First three books:", books[:3])
print("Last two books:", books[-2:])


librarian = {
    "Name": "Mr. Johnson",
    "Section": "Children's Library",
    "Experience": 8
}


librarian["Email"] = "johnson@library_community.com"

print("Librarian Details:", librarian)

print("Librarian Name:", librarian["Name"])
print("Library Section:", librarian["Section"])
print("Experience:", librarian["Experience"])
print("Email:", librarian["Email"])


book_numbers = [101, 102, 103, 104, 105, 106, 107]

books.sort()

book_directory = dict(zip(book_numbers, books))

print("Book Directory:", book_directory)

print("Book with Number 103:", book_directory[103])

if len(books) < 7:
    print("The library needs more books.")
else:
    print("The library has enough books.")


search = input("Enter a book name to search: ")

if search == "Harry Potter":
    print("Harry Potter is available in the library.")
elif search == "Diary of a Wimpy Kid":
    print("Diary of a Wimpy Kid is available in the library.")
elif search == "The Hobbit":
    print("The Hobbit is available in the library.")
elif search == "Charlotte's Web":
    print("Charlotte's Web is available in the library.")
elif search == "Percy Jackson":
    print("Percy Jackson is available in the library.")
elif search == "Wonder":
    print("Wonder is available in the library.")
else:
    print("This book is not available in the library.")