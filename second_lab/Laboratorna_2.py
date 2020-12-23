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

