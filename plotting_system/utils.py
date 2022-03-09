import pandas


def extract_file(directory):
    """
    :param directory: Directory to csv file you wish to plotting_system
    :return:
    """
    output_file = pandas.read_csv(directory, header=None, delim_whitespace=True,
                                  )

    return output_file


def calculate_energy(position, velocity):
    """
    :param position: position of ball over time
    :param velocity: velocity of ball over time
    :return: total energy of ball overtime
    """
    potential_energy = -position * 9.8
    kinetic_energy = 0.5 * (velocity ** 2)
    energy = potential_energy + kinetic_energy
    return energy
