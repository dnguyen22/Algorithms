# HW2: QuickSort


def choose_pivot(a_list, list_len):
    return a_list[0]


def quick_sort(a_list, list_len):
    # Base case
    if list_len < 2:
        # Return list and number of comparisons
        return a_list, 0
    else:
        pivot = choose_pivot(a_list, list_len)

        return a_list, 0

intArray = []
with open(''
          'QuickSort.txt') as f:
    for line in f:
        intArray.append(int(line))

# Print out array to make sure reading file worked
print(intArray)
print(len(intArray))