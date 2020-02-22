
import matplotlib.pyplot as plt

from die import Die


die_1 = Die()
die_2 = Die()
while True:
    plt.figure(figsize=(10, 6))

    results = []
    for roll_num in range(1000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    point_numbers = list(range(2, max_result+1))

    print(len(frequencies), len(point_numbers))

    plt.scatter(point_numbers, frequencies, s=30)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break