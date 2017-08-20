# HW1: Count Inversions


def sort_and_count_inversions(a_list, list_len):
    if list_len < 2:
        return a_list, 0
    else:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        left_tuple = sort_and_count_inversions(left_half, len(left_half))
        right_tuple = sort_and_count_inversions(right_half, len(right_half))
        split_tuple = merge_and_count_split_inversions(left_tuple[0], right_tuple[0])

        return split_tuple[0], left_tuple[1] + right_tuple[1] + split_tuple[1]


def merge_and_count_split_inversions(a_list, b_list):
    sorted_list = []
    count_inversions = 0
    i = 0
    j = 0

    while i < len(a_list) and j < len(b_list):
        if a_list[i] <= b_list[j]:
            sorted_list.append(a_list[i])
            i += 1
        else:
            sorted_list.append(b_list[j])
            j += 1
            count_inversions += len(a_list) - i

    while i < len(a_list):
        sorted_list.append(a_list[i])
        i += 1

    while j < len(b_list):
        sorted_list.append(b_list[j])
        j += 1

    return sorted_list, count_inversions

intArray = []
with open('IntegerArray.txt') as f:
    for line in f:
        intArray.append(int(line))

print(intArray)
print(sort_and_count_inversions(intArray, len(intArray))[0])
print(sort_and_count_inversions(intArray, len(intArray))[1])
