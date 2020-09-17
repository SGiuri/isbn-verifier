def is_valid(isbn):
    # 3-598-21508-8
    isbn_cypre = []
    for number in isbn:
        if number.isdecimal():
            isbn_cypre.append(int(number))
    if isbn[-1] == "X":
        isbn_cypre.append((10))
    print(isbn_cypre)
    pass

is_valid("3-598-21508-8")