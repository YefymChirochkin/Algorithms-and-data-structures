# Laboratory work 3

Outsourcing company (one of the market leaders) is preparing for the corporate event. The HR department sent a questionnaire about the types of beer that can be distributed on holidays. Mostly employees of the company like a few types of beer, and will be very offended if at least one of the beers they love is not at the party. Because you are the market leader, you cannot offend employees.On the other hand, buying all possible types of beer is expensive. 
My task will be to find out how many different types of beer you will need to bring to the corporate party.

## Incoming data
The first line contains the numbers **N** - the number of employees and **B** - the number of available beers. The second line contains **N * B** letters N or Y. If the letter **i * N + j** - Y, then employee **i** likes beer **j**.

## Output data
The smallest number of beers that should be on holiday.

## How to run code
1). Clone this repository git clone - https://github.com/YefymChirochkin/Algorithms-and-data-structures.git
2). cd Algorithms-and-data-structures/third_lab
2). And use command - python3 Laboratorna_3.py 

## Usage

```python
def main():
    input_string = "YNY YNY YNY NYY NYY NYN"
    people = string_to_people(input_string)
    tree = Tree()
    for person in people:
        tree.add_person(person)

    for person in tree.people:
        print(person)

    print(tree.find_the_shortest_way())

if __name__ == "__main__":
    main()
