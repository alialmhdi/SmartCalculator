number_of_books = int(input())
list_of_books = []
for _i in range(number_of_books):
    user_input = input().split(" ", 1)
    if len(user_input) > 1:
        action, book_name = user_input
        if action == "BUY":
            list_of_books.append(book_name)
    elif len(user_input) == 1:
        if user_input[0] == "READ":
            print(list_of_books.pop())
