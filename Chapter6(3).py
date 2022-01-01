def counter():
    word = input("Enter a word - ")
    let = input("Enter a letter - ")
    count = 0
    for letter in word:
        if letter == let:
            count += 1
    print(count)


counter()

