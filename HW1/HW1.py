# HW1: Count Inversions

def count_inversions(list):
    


intArray = []
with open('IntegerArray.txt') as f:
    for line in f:
        intArray.append(int(line))

print(intArray)
print(count_inversions(intArray))