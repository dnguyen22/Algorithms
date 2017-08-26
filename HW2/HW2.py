# HW2: QuickSort


def choose_pivot(a_list, start, end):
    return start


def quick_sort(a_list, start, end):
    # Base case
    if start >= end:
        # Return list and number of comparisons
        return 0
    else:
        pivot = choose_pivot(a_list, start, end)

        # Partition list around pivot
        # Move pivot to start of list
        if pivot != start:
            temp = a_list[start]
            a_list[start] = a_list[pivot]
            a_list[pivot] = temp
            pivot = start

        # Index of list of the first value bigger than pivot out of values looked at in the for loop
        pivot_boundary = start+1;

        for index in range(start, end):
            if a_list[index] < a_list[pivot]:
                temp = a_list[index]
                a_list[index] = a_list[pivot_boundary]
                a_list[pivot_boundary] = temp
                pivot_boundary = pivot_boundary + 1

        # Move pivot into correct location in list
        temp = a_list[pivot_boundary-1]
        a_list[pivot_boundary-1] = a_list[pivot]
        a_list[pivot] = temp

        left_side = quick_sort(a_list, start, pivot_boundary-1)
        right_side = quick_sort(a_list, pivot_boundary, end)

        return 0

intArray = [3, 8, 2, 5, 1, 4, 7, 6]
#with open(''
#          'QuickSort.txt') as f:
#    for line in f:
#        intArray.append(int(line))

# Print out array to make sure reading file worked
print(intArray)
print(len(intArray))
quick_sort(intArray, 0, len(intArray))
print(intArray)