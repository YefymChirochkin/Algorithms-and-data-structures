from Tree import Tree
from String_to_people import string_to_people

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