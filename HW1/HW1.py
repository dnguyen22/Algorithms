# HW1: Count Inversions

def count_inversions(a_list, list_len):
    if list_len == 0:
        return 0
    else:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        left_count = count_inversions(left_half, len(left_half))
        right_count = count_inversions(right_half, len(right_half))
        split_count = count_split_inversions(a_list, mid)

        return left_count + right_count + split_count

def count_split_inversions(a_list, list_len):
    return 0

intArray = []
with open('IntegerArray.txt') as f:
    for line in f:
        intArray.append(int(line))

print(intArray)
print(len(intArray))
print((len(intArray))//2)
# print(count_inversions(intArray, len(intArray)))