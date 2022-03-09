import os

import matplotlib.pyplot as plt
from numpy import sqrt

from plotting_system.utils import extract_file, calculate_energy

current_path = os.getcwd()


def plot_ball(directory, name_of_file, directory_to_save=current_path + '/figs/', ):
    """
    :param name_of_file: name of file you wish to save
    :param directory_to_save: directory to save file
    :param directory: Directory to csv file you wish to plotting_system
    :return: None
    """
    # import data
    output_file = extract_file(directory)
    # extract relevant information
    time, position, velocity = output_file[0].values, output_file[1].values, output_file[
        2].values
    total_energy = calculate_energy(position, velocity)

    # initial parameters
    initial_velocity = velocity[0]
    initial_position = position[0]


    # calculate theoretical maximum parameters
    k = -initial_velocity / -9.8
    max_position = 0.5 * (-9.8) * (k ** 2) + initial_velocity * k + initial_position
    max_velocity = sqrt(2 * 9.8 * max_position)
    max_energy = max_position * 9.8

    # plotting_system ball parameters
    fig, axs = plt.subplots(3, 1)

    axs[0].set_title('Ball Position vs Time')
    axs[0].set_xlabel('Time(seconds)')
    axs[0].set_ylabel('Position(meters)')
    axs[0].axhline(y=max_position, color='red', linestyle='--')
    axs[0].plot(time, position, color='olivedrab')

    axs[1].set_title('Ball Velocity vs Time')
    axs[1].set_xlabel('Time(seconds)')
    axs[1].set_ylabel('Velocity(meters per second)')
    axs[1].axhline(y=max_velocity, color='r', linestyle='--')
    axs[1].plot(time, velocity, color='indigo')

    axs[2].set_title('Ball Energy per mass vs Time')
    axs[2].set_xlabel('Time(seconds)')
    axs[2].set_ylabel('Energy(Joules/Kg)')
    axs[2].axhline(y=max_energy, color='red', linestyle='--')
    axs[2].plot(time, total_energy, color='indianred')

    fig.tight_layout()

    plt.plot()
    plt.savefig(directory_to_save + name_of_file)
