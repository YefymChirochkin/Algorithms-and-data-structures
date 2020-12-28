# Laboratory work 5

Boyer–Moore string-search algorithm is an efficient string-searching algorithm that is the standard benchmark for practical string-search literature. The original paper contained static tables for computing the pattern shifts without an explanation of how to produce them. The algorithm preprocesses the string being searched for (the pattern), but not the string being searched in (the text). It is thus well-suited for applications in which the pattern is much shorter than the text or where it persists across multiple searches. The Boyer–Moore algorithm uses information gathered during the preprocess step to skip sections of the text, resulting in a lower constant factor than many other string search algorithms. In general, the algorithm runs faster as the pattern length increases. The key features of the algorithm are to match on the tail of the pattern rather than the head, and to skip along the text in jumps of multiple characters rather than searching every single character in the text.

## How to run code
1). Clone this repository git clone - https://github.com/YefymChirochkin/lab_4.git

2). cd lab_5

3). And use command - python3 laboratorna_5.py

## Usage

```python
from boyer_moore_algorithm import BoyerMoore


def main():
    input_string = BoyerMoore("The original paper contained static tables for computing the pattern shifts "
                              "without an explanation of how to produce them")
    print(input_string.boyer_moore_search("shifts"))


if __name__ == '__main__':
    main()