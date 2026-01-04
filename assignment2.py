import numpy as np

def stat():
    data = np.loadtxt("populations.txt")

    hare = data[:, 1]

    min_index = np.argmin(hare)
    min_year_hare = int(data[min_index, 0])

    lynx = data[:, 2]
    lynx_avg = np.mean(lynx)

    species_sum = data[:, 1] + data[:, 2] + data[:, 3]
    new_data = np.column_stack((data, species_sum))

    new_data[new_data[:, 3] < 40000, 3] = 0

    return data, hare, min_year_hare, lynx_avg, new_data

