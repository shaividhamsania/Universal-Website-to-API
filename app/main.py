"""from extractors.wikipedia import search_wikipedia


if __name__ == "__main__":

    result = search_wikipedia(
        "Artificial_intelligence",
        3
    )

    print(result)"""


"""from extractors.quotes import extract_quotes


if __name__ == "__main__":

    results = extract_quotes()

    for item in results:
        print(item)"""


from extractors.books import extract_books


if __name__ == "__main__":

    results = extract_books()

    for book in results:
        print(book)