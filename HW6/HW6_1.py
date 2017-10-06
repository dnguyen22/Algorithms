# HW6_1: 2-Sum Algorithm


# Returns set from text file of integer values. Since a set is implemented the same as dictionaries, we get O(1) inserts
#   and O(1) lookups
def extract_data(file):
    input_integers = set()
    with open(file) as f:
        for line in f:
            input_integers.add(int(line))
    return input_integers


input_ints = extract_data('algo1-programming_prob-2sum.txt')
# List holding all of the targets where x+y=target and x and y are distinct values in input_ints
two_sum_success = []

for t in range(-10000, 10001):
    for number in input_ints:
        # Find complement of target
        complement = t - number
        # Search for complement in input_ints
        if complement in input_ints and complement != number:
            two_sum_success.append(t)
            break

print(two_sum_success)
print(len(two_sum_success))