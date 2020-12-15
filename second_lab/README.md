# Laboratory work 2

Farmer John built a new long detachment for cattle, with N (2 <= N <= 100,000) sections. 
The sections are located along a straight line in positions x1, ..., xN (0 <= x-i <= 1 000 000 000).
His C (2 <= C <= N) cows do not like the new building and become aggressive towards each other when they are placed in adjacent stalls. 
To avoid situations where cows may harm each other, the farmer wants to place aggressive cows in stalls so that the minimum distance between any of them is as large as possible.

## How to run code
1). Clone this repository git clone - https://github.com/YefymChirochkin/Algorithms-and-data-structures.git
2). cd Algorithms-and-data-structures/second_lab
2). And use command - python3 Laboratorna_2.py 

## Usage

```python
def check_data(array, value, angry_cows):
    counter = 1
    temporary_array = array[0]
    for i in range(len(array)):
        if array[i] - temporary_array >= value:
            counter += 1
            temporary_array = array[i]
            if counter >= angry_cows:
                return True
    return False


number_of_angry_cows = 3
example_array = [1, 2, 4, 8, 9]
example_array.sort()
right_index = example_array[len(example_array) - 1]
left_index = 1
result = 0
while left_index < right_index:
    middle_index = left_index + (right_index - left_index) // 2
    if check_data(example_array, middle_index, number_of_angry_cows):
        result = middle_index
        left_index = middle_index + 1
    else:
        right_index = middle_index
print(f"The minimum value of the maximum distance is: {str(result)}")
