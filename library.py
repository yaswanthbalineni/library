import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self):
        self.books = {}  
        self.users = {}  
    
    def add_book(self, book_id, book_name, quantity):
        """Add a book to the library."""
        if book_id in self.books:
            self.books[book_id][1] += quantity  # Increase available quantity if book exists
        else:
            self.books[book_id] = [book_name, quantity]
        messagebox.showinfo("Success", f'Book "{book_name}" added successfully.')
    
    def borrow_book(self, user_id, book_id):
        """Allow a user to borrow a book."""
        if book_id not in self.books or self.books[book_id][1] == 0:
            messagebox.showerror("Error", "Sorry, the book is not available.")
            return
        if user_id not in self.users:
            self.users[user_id] = [input("Enter your name: "), []]  
        book_name = self.books[book_id][0]
        self.books[book_id][1] -= 1  
        self.users[user_id][1].append(book_name)  
        messagebox.showinfo("Success", f"Book '{book_name}' borrowed successfully!")
    
    def return_book(self, user_id, book_id):
        """Allow a user to return a book."""
        if user_id not in self.users or book_id not in self.books:
            messagebox.showerror("Error", "Invalid user or book ID.")
            return
        book_name = self.books[book_id][0]
        if book_name in self.users[user_id][1]:
            self.users[user_id][1].remove(book_name)  
            self.books[book_id][1] += 1  
            messagebox.showinfo("Success", f"Book '{book_name}' returned successfully!")
        else:
            messagebox.showerror("Error", f"You have not borrowed '{book_name}'.")

    def view_user_books(self, user_id):
        """View all borrowed books of a user."""
        if user_id in self.users:
            user_name = self.users[user_id][0]
            borrowed_books = self.users[user_id][1]
            if borrowed_books:
                book_list = '\n'.join(borrowed_books)
                messagebox.showinfo(f"{user_name}'s Borrowed Books", book_list)
            else:
                messagebox.showinfo(f"{user_name}'s Borrowed Books", "No books borrowed.")
        else:
            messagebox.showerror("Error", "User not found.")
        
    def display_books(self):
        """Return all books in the library."""
        book_list = ""
        if self.books:
            for book_id, (book_name, quantity) in self.books.items():
                book_list += f"ID: {book_id}, Name: {book_name}, Quantity: {quantity}\n"
        else:
            book_list = "No books available."
        return book_list

# GUI for the Library Management System
class LibraryApp:
    def __init__(self, root, library):
        self.library = library
        self.root = root
        self.root.title("Library Management System")

        # Create the input fields and buttons
        self.create_widgets()

    def create_widgets(self):
        # Add Book section
        self.add_book_label = tk.Label(self.root, text="Add a Book", font=("Arial", 14))
        self.add_book_label.grid(row=0, column=0, padx=10, pady=10)

        self.book_id_label = tk.Label(self.root, text="Book ID:")
        self.book_id_label.grid(row=1, column=0, padx=10)
        self.book_id_entry = tk.Entry(self.root)
        self.book_id_entry.grid(row=1, column=1, padx=10)

        self.book_name_label = tk.Label(self.root, text="Book Name:")
        self.book_name_label.grid(row=2, column=0, padx=10)
        self.book_name_entry = tk.Entry(self.root)
        self.book_name_entry.grid(row=2, column=1, padx=10)

        self.book_qty_label = tk.Label(self.root, text="Quantity:")
        self.book_qty_label.grid(row=3, column=0, padx=10)
        self.book_qty_entry = tk.Entry(self.root)
        self.book_qty_entry.grid(row=3, column=1, padx=10)

        self.add_book_button = tk.Button(self.root, text="Add Book", command=self.add_book)
        self.add_book_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Borrow Book section
        self.borrow_book_label = tk.Label(self.root, text="Borrow a Book", font=("Arial", 14))
        self.borrow_book_label.grid(row=5, column=0, padx=10, pady=10)

        self.user_id_label = tk.Label(self.root, text="User ID:")
        self.user_id_label.grid(row=6, column=0, padx=10)
        self.user_id_entry = tk.Entry(self.root)
        self.user_id_entry.grid(row=6, column=1, padx=10)

        self.borrow_book_id_label = tk.Label(self.root, text="Book ID:")
        self.borrow_book_id_label.grid(row=7, column=0, padx=10)
        self.borrow_book_id_entry = tk.Entry(self.root)
        self.borrow_book_id_entry.grid(row=7, column=1, padx=10)

        self.borrow_button = tk.Button(self.root, text="Borrow Book", command=self.borrow_book)
        self.borrow_button.grid(row=8, column=0, columnspan=2, pady=10)

        # Return Book section
        self.return_book_label = tk.Label(self.root, text="Return a Book", font=("Arial", 14))
        self.return_book_label.grid(row=9, column=0, padx=10, pady=10)

        self.return_book_id_label = tk.Label(self.root, text="Book ID:")
        self.return_book_id_label.grid(row=10, column=0, padx=10)
        self.return_book_id_entry = tk.Entry(self.root)
        self.return_book_id_entry.grid(row=10, column=1, padx=10)

        self.return_button = tk.Button(self.root, text="Return Book", command=self.return_book)
        self.return_button.grid(row=11, column=0, columnspan=2, pady=10)

        # View Borrowed Books
        self.view_borrowed_books_label = tk.Label(self.root, text="View Borrowed Books", font=("Arial", 14))
        self.view_borrowed_books_label.grid(row=12, column=0, padx=10, pady=10)

        self.view_user_id_label = tk.Label(self.root, text="User ID:")
        self.view_user_id_label.grid(row=13, column=0, padx=10)
        self.view_user_id_entry = tk.Entry(self.root)
        self.view_user_id_entry.grid(row=13, column=1, padx=10)

        self.view_button = tk.Button(self.root, text="View Books", command=self.view_borrowed_books)
        self.view_button.grid(row=14, column=0, columnspan=2, pady=10)

        # Display all Books
        self.display_books_button = tk.Button(self.root, text="Display All Books", command=self.display_books)
        self.display_books_button.grid(row=15, column=0, columnspan=2, pady=10)

    def add_book(self):
        book_id = self.book_id_entry.get()
        book_name = self.book_name_entry.get()
        quantity = int(self.book_qty_entry.get())
        self.library.add_book(book_id, book_name, quantity)

    def borrow_book(self):
        user_id = self.user_id_entry.get()
        book_id = self.borrow_book_id_entry.get()
        self.library.borrow_book(user_id, book_id)

    def return_book(self):
        user_id = self.user_id_entry.get()
        book_id = self.return_book_id_entry.get()
        self.library.return_book(user_id, book_id)

    def view_borrowed_books(self):
        user_id = self.view_user_id_entry.get()
        self.library.view_user_books(user_id)

    def display_books(self):
        book_list = self.library.display_books()
        messagebox.showinfo("Books in Library", book_list)

def main():
    library = Library()
    root = tk.Tk()
    app = LibraryApp(root, library)
    root.mainloop()

if __name__ == "__main__":
    main()
