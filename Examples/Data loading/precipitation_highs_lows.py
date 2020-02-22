import csv

from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, precipitationIn = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            precipitation = float(row[19])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            precipitationIn.append(precipitation)

fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(dates, precipitationIn, c='red', alpha=0.5)
plt.title("Daily precipitation - 2014", fontsize=24)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Precipitation (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
