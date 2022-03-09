import os

from matplotlib import pyplot as plt
from numpy import sqrt

from plotting_system.utils import calculate_energy, extract_file

current_path = os.getcwd()


def plot_differences(directory1, directory2, name_of_file, directory_to_save=current_path + '/figs/', ):
    """
    :param directory1: Directory to first csv file you wish to plotting_system
    :param directory2: Directory to second csv file you wish to plotting_system
    :param name_of_file: name of file you wish to save
    :param directory_to_save: directory to save file
    :return: None
    """
    # import data
    output_files = [directory1, directory2]
    output_files = [extract_file(directory) for directory in output_files]

    # extract relevant information
    time = output_files[0][0]
    positions = [output_file[1] for output_file in output_files]
    velocities = [output_file[2] for output_file in output_files]

    energy_1 = calculate_energy(positions[0], velocities[0])
    energy_2 = calculate_energy(positions[1], velocities[1])


    # plotting_system ball parameters
    fig, axs = plt.subplots(3, 1)

    axs[0].set_title('Difference in Ball Position vs Time')
    axs[0].set_xlabel('Time(seconds)')
    axs[0].set_ylabel('Position(meters)')
    axs[0].plot(time, positions[0]-positions[1], color='olivedrab')

    axs[1].set_title('Difference in Ball Velocity vs Time')
    axs[1].set_xlabel('Time(seconds)')
    axs[1].set_ylabel('Velocity(meters per second)')
    axs[1].plot(time, velocities[0]-velocities[1], color='indigo')

    axs[2].set_title('Difference in Ball Energy per mass vs Time')
    axs[2].set_xlabel('Time(seconds)')
    axs[2].set_ylabel('Energy(Joules/Kg)')
    axs[2].plot(time, energy_1-energy_2, color='indianred')

    fig.tight_layout()

    plt.plot()
    plt.savefig(directory_to_save + name_of_file)
