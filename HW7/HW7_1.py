# HW7_1: Job Scheduling - Greedy Algorithms
from operator import attrgetter


# Creates a job class that has a job weight and job length
class Job:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
        self.priority = self.get_difference()

    # Print out weight and length of Job
    def __repr__(self):
        return repr((self.weight, self.length))

    # Returns weight - length for scheduling purposes
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
            jobs.append(Job(int(split[0]), int(split[1])))
    return jobs


# Get jobs from file
jobs = extract_data('jobs.txt')
# Print list of jobs
print(jobs)
# Print jobs sorted by highest priority (based on difference), then by weight in case of tie
sorted_jobs = sorted(jobs, reverse=True, key=attrgetter('priority', 'weight'))
print(sorted_jobs)
# Initialize variables for computing sum weighted completion time
completion_time = 0
sum_weighted_completion = 0
# Loop through jobs to calculate sum weighted completion time
for job in jobs:
    completion_time = completion_time + job.length
    sum_weighted_completion = sum_weighted_completion + job.weight * completion_time

print(sum_weighted_completion)