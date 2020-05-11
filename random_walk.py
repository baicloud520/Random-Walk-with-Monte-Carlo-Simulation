import matplotlib.pyplot as plt
from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, steps):
        """Initialize attributes of RandomWalk."""
        self.num_points = steps
        self.x_values = [0]
        self.y_values = [0]
        self.CRITERION = 4

    def fill_walk(self):
        """Generate all possible steps in the random walk."""

        for i in range(self.num_points):
            direction = {
            "N": choice([1]),
            "S": choice([-1]),
            "E": choice([1]),
            "W": choice([-1])
            }

            (dx, dy) = choice([(0, direction["N"]), (0, direction["S"]),
                (direction["E"], 0), (direction["W"], 0)])

            # Update x-, and y-coordinates.
            x = self.x_values[-1] + dx
            y = self.y_values[-1] + dy

            # Append new value to a list of x-, and y- coordinates.
            self.x_values.append(x)
            self.y_values.append(y)

    # def fill_walk(self):
    #     """Generate all possible steps in a ranndom walk."""

    #     for i in range(self.num_points):
    #         direction = {
    #             "N": choice([1]),
    #             "S": choice([-1]),
    #             "E": choice([1]),
    #             "W": choice([-1])
    #         }

    #         (dx, dy) = choice([(0, direction["N"]), (0, direction["S"]),
    #                            (direction["E"], 0), (direction["W"], 0)])

    #         x = self.x_values[-1] + dx
    #         y = self.y_values[-1] + dy

    #         self.x_values.append(x)
    #         self.y_values.append(y)

    def calculate_distance(self, no_transport, sum_distance):
        """
        For each step in the range of available steps, calculate the
        distance between starting and ending points.
        """

        distance = abs(self.x_values[-1]) + abs(self.y_values[-1])
        sum_distance += distance
        if distance <= self.CRITERION:
            no_transport += 1
        return(no_transport, sum_distance)

    def calculate_average(self, sum_distance, tests, no_transport,
                          average_distances, tot_percentages):
        """ Estimate average distances and probability."""

        average_distance = round(float(sum_distance) / tests, 2)
        average_distances.append(average_distance)

        no_transport_percentage = round(
            100 * (float(no_transport) / tests), 2)
        tot_percentages.append(no_transport_percentage)
        return(average_distances, tot_percentages)

    def plot_walk(self, step, test, step_counter, average_distances,
                  tot_percentages):
        """Plot the graphs."""

        # Initialize plot.
        plt.style.use("grayscale")
        fig, axs = plt.subplots(
            2, 2, False, False, figsize=(11, 7))
        point_numbers = range(self.num_points)

        axs[0, 0].scatter(self.x_values, self.y_values, c=self.x_values,
                          cmap=plt.cm.Blues, edgecolors="black", s=25)
        axs[0, 1].scatter(self.x_values, self.y_values, c=self.x_values,
                          cmap=plt.cm.Blues, edgecolors="black", s=50)
        axs[1, 0].scatter(step_counter, average_distances, c=step_counter,
                          cmap=plt.cm.Blues, edgecolors="black", s=50)
        axs[1, 1].scatter(step_counter, tot_percentages, c=step_counter,
                          cmap=plt.cm.Blues, edgecolors="black", s=50)

        # Customize title, labels, and tick parameters.
        fig.suptitle(
            f"Random walk: Walk-{step} | Test-{test}", fontsize=20)

        axs[0, 0].set_xlabel("Steps along x-direction, [-]", fontsize=10)
        axs[0, 0].set_ylabel("Steps along y-direction, [-]", fontsize=10)

        axs[0, 1].set_xlabel("Steps along x-direction, [-]", fontsize=10)
        axs[0, 1].set_ylabel("Steps along y-direction, [-]", fontsize=10)

        axs[1, 0].set_xlabel("Tot. number of steps, [-]", fontsize=10)
        axs[1, 0].set_ylabel("Average distance, [-]", fontsize=10)

        axs[1, 1].set_xlabel("Tot. number of steps, [-]", fontsize=10)
        axs[1, 1].set_ylabel(f"P(Av. distance<={self.CRITERION}), [%]",
                             fontsize=10)

        for ax in axs.flat:
            ax.tick_params(axis="both", which="major", labelsize=10)

        # Fix range for x-, and y-axis (Optional).
        axs[0, 0].axis([-15, 15, -15, 15])
        axs[1, 0].axis([0, 31, 0, 8])
        axs[1, 1].axis([0, 31, 0, 110])

        # Display plot.
        plt.show()
