import random


def quick_sort(array: list, reverse: bool = False) -> list:
    sorted_array = array[:]

    if len(sorted_array) == 0:
        return sorted_array

    pivot = sorted_array[0]

    lower_array = [element for element in sorted_array if element < pivot]
    higher_array = [element for element in sorted_array if element > pivot]

    if not reverse:
        return (
                quick_sort(lower_array) +
                [element for element in sorted_array if element == pivot] +
                quick_sort(higher_array)
        )
    return (
            quick_sort(higher_array, reverse) +
            [element for element in sorted_array if element == pivot] +
            quick_sort(lower_array, reverse)
    )


array = [random.randint(0, 200) for i in range(0, 200)]

print(quick_sort(array), "\n")
print(quick_sort(array, reverse=True))
