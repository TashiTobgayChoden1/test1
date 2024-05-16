# initiate empty list, set and dictionary
books_list=[]
authors_set=set()
books_dict={}
#add books
books_list.append("Python Programming")
authors_set.add("John Smith")
books_dict["Python Programming"]="John Smith"

books_list.append("Data structures and algorithms")
authors_set.add("Jane Doe")
books_dict["Data structure and algorithms"]="Jane Doe"

books_list.append("Machine learning Basics")
authors_set.add("Alice Johnson")
books_dict["Machine learning Basics"]="ALice Johnson"

#search for a book
search_title=input("Enter the title of the book to search:")
if search_title in books_list:
    print(f"Book found! Author:{books_dict[search_title]}")
else:
    print("Books not found!")

#Display all books
print("Lists of books:")
for book in books_list:
    print(book)

#remove a book
remove_title=input("Enter the title of the book to remove or else enter to skip:")
if remove_title in books_list:
    remove_author=books_dict[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("Book removed succesfully!")
    print("Bppks available:",books_list)
else:
    print("Books not found!")