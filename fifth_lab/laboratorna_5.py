from boyer_moore_algorithm import BoyerMoore


def main():
    input_string = BoyerMoore("The original paper contained static tables for computing the pattern shifts "
                              "without an explanation of how to produce them")
    print(input_string.boyer_moore_search("shifts"))


if __name__ == '__main__':
    main()