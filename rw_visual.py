import sys
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Ask user at the end of simulation to continue or
# to quit program.
while True:

    steps = 32
    tests = 20_001
    average_distances = []
    tot_percentages = []
    step_counter = []

    for step in range(1, steps):
        no_transport = 0
        sum_distance = 0

        for test in range(1, tests):
            rw = RandomWalk(step)
            rw.fill_walk()
            (no_transport, sum_distance) = rw.calculate_distance(
                no_transport, sum_distance)

        (average_distances, tot_percentages) = rw.calculate_average(
            sum_distance, tests, no_transport, average_distances,
            tot_percentages)

        step_counter.append(step)
        rw.plot_walk(step, test, step_counter, average_distances,
                     tot_percentages)

    # Generate new random walk?
    keep_running = input("Make another random walk? (y/n): ")
    if keep_running == "n":
        sys.exit()
