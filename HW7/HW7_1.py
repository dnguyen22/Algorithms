# HW7_1: Job Scheduling - Greedy Algorithms


# Creates a job class that has a job weight and job length
class Job:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length

    def get_difference(self):
        return self.weight - self.length


# Returns list from text file of integer tuples (job weight, job length).
def extract_data(file):
    jobs = []
    with open(file) as f:
        # Skip first line (header)
        j = f.readlines()[1:]
        for line in j:
            split = line.split()
            jobs.append((int(split[0]), int(split[1])))
    return jobs


# Get jobs from file
jobs = extract_data('jobs.txt')
print(jobs)