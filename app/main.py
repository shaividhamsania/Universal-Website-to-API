from extractors.wikipedia import search_wikipedia


if __name__ == "__main__":

    result = search_wikipedia(
        "Artificial_intelligence",
        3
    )

    print(result)