import csv

from datetime import datetime
from matplotlib import pyplot as plt


def get_data(filename):
    dates, highs, lows = [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append((high - 32) / 1.8)
                lows.append((low - 32) / 1.8)
    return dates, highs, lows


def print_lines(dates, highs, lows, c_1='red', c_2='blue'):
    plt.plot(dates, highs, c=c_1, alpha=0.5)
    plt.plot(dates, lows, c=c_2, alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    return 0


file_1 = 'sitka_weather_2014.csv'
file_2 = 'death_valley_2014.csv'

dates_1, highs_1, lows_1 = get_data(file_1)
dates_2, highs_2, lows_2 = get_data(file_2)

fig = plt.figure(dpi=128, figsize=(10, 6))

print_lines(dates_1, highs_1, lows_1)
print_lines(dates_2, highs_2, lows_2, c_1='yellow', c_2='green')

plt.ylim(0, 50)

plt.title("Daily high temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
