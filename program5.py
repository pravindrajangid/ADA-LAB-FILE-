
from dataclasses import dataclass
from typing import List


# Fractional Knapsack

def fractional_knapsack(weights: List[int], values: List[int], capacity: int) -> float:
    items = []

    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    # Highest value/weight ratio first
    items.sort(reverse=True)

    total_profit = 0.0
    remaining = capacity

    for ratio, weight, value in items:
        if remaining == 0:
            break

        if weight <= remaining:
            total_profit += value
            remaining -= weight
        else:
            fraction = remaining / weight
            total_profit += value * fraction
            remaining = 0

    return total_profit


# Job Scheduling

@dataclass
class Job:
    id: int
    deadline: int
    profit: int


def job_scheduling(jobs: List[Job]) -> List[int]:
    jobs.sort(key=lambda job: job.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)

    slots = [False] * (max_deadline + 1)

    sequence = []

    for job in jobs:
        for slot in range(job.deadline, 0, -1):
            if not slots[slot]:
                slots[slot] = True
                sequence.append(job.id)
                break

    return sequence


# Main Program

# Fractional Knapsack
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

profit = fractional_knapsack(weights, values, capacity)

print("Fractional Knapsack")
print("Maximum Profit =", profit)


# Job Scheduling
jobs = [
    Job(1, 2, 100),
    Job(2, 1, 19),
    Job(3, 2, 27),
    Job(4, 1, 25),
    Job(5, 3, 15)
]

sequence = job_scheduling(jobs)

print("\nJob Scheduling")
print("Optimal Job Sequence =", sequence)
