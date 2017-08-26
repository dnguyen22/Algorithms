# HW2: QuickSort


def choose_pivot(a_list, start, end):
    middle = ((end-1)-start)//2 + start
    medians = [a_list[start], a_list[end-1], a_list[middle]]
    return a_list.index(sorted(medians)[1])


def set_final_element_pivot(a_list, start, end):
    return start


def set_final_element_pivot(a_list, start, end):
    return end-1


def quick_sort(a_list, start, end):
    # Base case
    if start >= end:
        # Return number of comparisons
        return 0
    else:
        # Set pivot as first element
        #pivot = set_first_element_pivot(a_list, start, end)
        # Set pivot as final element
        #pivot = set_final_element_pivot(a_list, start, end)
        # Set pivot as median of medians
        pivot = choose_pivot(a_list, start, end)

        # Partition list around pivot
        # Move pivot to start of list
        if pivot != start:
            temp = a_list[start]
            a_list[start] = a_list[pivot]
            a_list[pivot] = temp
            pivot = start

        # Index of list of the first value bigger than pivot out of values looked at in the for loop
        pivot_boundary = start + 1

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

        return (end-start) - 1 + left_side + right_side

intArray = []
with open(''
          'QuickSort.txt') as f:
    for line in f:
        intArray.append(int(line))

# Print out array to make sure reading file worked
# Not 150724; 159894
print(intArray)
print(len(intArray))
print(quick_sort(intArray, 0, len(intArray)))
print(intArray)
