class Farm:

    def __init__(self, location: str, number_of_animals: int, fan_power_watts: float):
        self.location = location
        self.number_of_animals = number_of_animals
        self.fan_power_watts = fan_power_watts

    @staticmethod
    def heapify(array, size_of_array, index_of_parent):
        index_of_largest_element = index_of_parent
        index_of_left_child = 2 * index_of_parent + 1
        index_of_right_child = 2 * index_of_parent + 2
        if index_of_left_child < size_of_array and array[index_of_parent].number_of_animals < array[index_of_left_child].number_of_animals:
            index_of_largest_element = index_of_left_child
        if index_of_right_child < size_of_array and array[index_of_largest_element].number_of_animals < array[index_of_right_child].number_of_animals:
            index_of_largest_element = index_of_right_child
        if index_of_largest_element != index_of_parent:
            array[index_of_parent], array[index_of_largest_element] = array[index_of_largest_element], array[index_of_parent]
            Farm.heapify(array, size_of_array, index_of_largest_element)

    @staticmethod
    def sort_farm_number_of_animals_by_ascending(array):
        for i in range(len(array) // 2 - 1, -1, -1):
            Farm.heapify(array, len(array), i)
        for i in range(len(array) - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            Farm.heapify(array, i, 0)

    @staticmethod
    def intermediate_result_farm_number_of_animals(array):
        for element in array:
            print(element.number_of_animals)
        print("***************")

    @staticmethod
    def sort_farm_fan_power_watts_by_descending(array):
        for i in range(len(array) - 1):
            swapped = False
            for j in range(0, len(array) - i - 1):
                if array[j].fan_power_watts < array[j + 1].fan_power_watts:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapped = True
            if not swapped:
                break

    @staticmethod
    def intermediate_result_farm_fan_power_watts(array):
        for element in array:
            print(element.fan_power_watts)
        print("***************")


if __name__ == "__main__":
    first_farm = Farm("First farm", 2030, 1234.4)
    second_farm = Farm("Second farm", 4235, 16.8)
    third_farm = Farm("Third farm", 1230, 9.4)
    fourth_farm = Farm("Fourth farm", 1405, 45.8)
    fifth_farm = Farm("Fifth farm", 5667, 33.4)
    sixth_farm = Farm("Sixth farm", 3436, 3.8)
    seventh_farm = Farm("Seventh farm", 7526, 235.4)
    array_of_farms = [first_farm, second_farm, third_farm, fourth_farm, fifth_farm, sixth_farm, seventh_farm]

    Farm.intermediate_result_farm_number_of_animals(array_of_farms)
    Farm.sort_farm_number_of_animals_by_ascending(array_of_farms)
    Farm.intermediate_result_farm_number_of_animals(array_of_farms)

    Farm.intermediate_result_farm_fan_power_watts(array_of_farms)
    Farm.sort_farm_fan_power_watts_by_descending(array_of_farms)
    Farm.intermediate_result_farm_fan_power_watts(array_of_farms)


