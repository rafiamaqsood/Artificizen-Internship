from library import Library

library = Library()

# Load saved data
library.load_data()


def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_positive_integer(message):
    while True:
        try:
            number = int(input(message))

            if number <= 0:
                print("Please enter a number greater than 0.")
                continue

            return number

        except ValueError:
            print("Please enter a valid integer.")


def get_isbn():
    while True:
        isbn = input("Enter ISBN: ").strip()

        if not isbn:
            print("ISBN cannot be empty.")
            continue

        if not isbn.isdigit():
            print("ISBN should contain only digits.")
            continue

        return isbn


def get_member_id():
    while True:
        member_id = input("Enter member ID: ").strip()

        if not member_id:
            print("Member ID cannot be empty.")
            continue

        return member_id


def get_menu_choice():
    while True:
        choice = input("Enter your choice: ").strip()

        if choice in ["1", "2", "3", "4", "5", "6", "7" , "8"]:
            return choice

        print("Invalid choice. Please enter a number from 1 to 8.")


while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. View All Books")
    print("7. View All Members")
    print("8. Exit")

    choice = get_menu_choice()

    try:

        if choice == "1":
            title = get_non_empty_input("Enter book title: ")
            author = get_non_empty_input("Enter author name: ")
            isbn = get_isbn()
            copies = get_positive_integer("Enter number of copies: ")

            library.add_book(title, author, isbn, copies)

        elif choice == "2":
            name = get_non_empty_input("Enter member name: ")
            member_id = get_member_id()

            library.add_member(name, member_id)
        
        elif choice == "3":

            print("\nSearch Book By")
            print("1. ISBN")
            print("2. Title")

            search_choice = input("Enter your choice: ").strip()

            if search_choice == "1":
                isbn = get_isbn()
                book = library.search_book_by_isbn(isbn)

            elif search_choice == "2":
                title = get_non_empty_input("Enter book title: ")
                book = library.search_book_by_title(title)

            else:
                print("Invalid choice.")
                continue

            print("\nBook Found")
            print(book)

        elif choice == "4":
            member_id = get_member_id()
            isbn = get_isbn()

            library.issue_book(member_id, isbn)

        elif choice == "5":
            member_id = get_member_id()
            isbn = get_isbn()

            library.return_book(member_id, isbn)
        elif choice == "6":
            library.display_books()

        elif choice == "7":
            library.display_members()

        elif choice == "8":
            library.save_data()
            print("Thank you for using the Library Management System!")
            break
    except Exception as e:
        print("Error:", e)