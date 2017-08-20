# HW1: Count Inversions


def sort_and_count_inversions(a_list, list_len):
    # Base case
    if list_len < 2:
        return a_list, 0
    else:
        # Divide list in half for divide and conquer
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        # Recursive calls for left and right halves of list
        left_tuple = sort_and_count_inversions(left_half, len(left_half))
        right_tuple = sort_and_count_inversions(right_half, len(right_half))
        # Merge two sorted lists together
        split_tuple = merge_and_count_split_inversions(left_tuple[0], right_tuple[0])

        # Return sorted list and number of inversions
        return split_tuple[0], left_tuple[1] + right_tuple[1] + split_tuple[1]


# Merge portion of merge sort algorithm
def merge_and_count_split_inversions(a_list, b_list):
    sorted_list = []
    count_inversions = 0
    i = 0
    j = 0

    # Add smallest value from each of the two sorted list to new list
    while i < len(a_list) and j < len(b_list):
        if a_list[i] <= b_list[j]:
            sorted_list.append(a_list[i])
            i += 1
        else:
            sorted_list.append(b_list[j])
            j += 1
            # Count inversions when items from second list are added before first
            count_inversions += len(a_list) - i

    # Clean up. Add remainder of first list if second list finishes early
    while i < len(a_list):
        sorted_list.append(a_list[i])
        i += 1

    # Clean up. Add remainder of second list if first list finishes early
    while j < len(b_list):
        sorted_list.append(b_list[j])
        j += 1

    return sorted_list, count_inversions

intArray = []
with open('IntegerArray.txt') as f:
    for line in f:
        intArray.append(int(line))

# Print out array to make sure reading file worked
print(intArray)
# Print sorted array
print(sort_and_count_inversions(intArray, len(intArray))[0])
# Print number of inversions
print(sort_and_count_inversions(intArray, len(intArray))[1])
