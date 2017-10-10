# HW9_2: Weighted Independent Sets - Dynamic Programming Intro


# Loops through file and adds vertices to UnionFind
def extract_data(file):
    weights = []
    with open(file) as f:
        # Skip first line (header)
        j = f.readlines()[1:]
        for line in j:
            weights.append((int(line), index))
            index = index + 1
    return weights


vertices = extract_data('mwis.txt')
