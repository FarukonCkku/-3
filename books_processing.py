def get_books(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')[1:] 
    return list(map(
        lambda line: list(map(
            lambda x: float(x) if '.' in x else int(x) if x.isdigit() else x,
            line.split('|')
        )),
        filter(lambda line: line.strip(), lines)
    ))

def filtered_books(books, substring):
    return list(map(
        lambda book: [book[0], f"{book[1]}, {book[2]}", book[3], book[4]],
        filter(lambda book: substring.lower() in book[1].lower(), books)
    ))

def get_totals(books):
    return list(map(
        lambda book: (book[0], book[2] * book[3]),
        books
    ))
