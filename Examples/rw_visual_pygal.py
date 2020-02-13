import pygal

from random_walk import RandomWalk

while True:
    rw = RandomWalk(2000)
    rw.fill_walk()
    frequencies = []

    for i in range(rw.num_points):
        frequencies.append((rw.x_values[i], rw.y_values[i]))

    hist = pygal.XY(stroke=False)

    hist.title = "Correlation"
    hist.add('D6 + D6', frequencies)
    hist.render_to_file('RW_vis.svg')

    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break
