from luna import *
import datetime
import matplotlib.pyplot as plt
import numpy

now = datetime.datetime.now()

def altitude(date):
    home = Luna(45.406027, -122.677563)
    return home.calculate(date.year, date.month, date.day,
                          date.hour, date.minute, date.second)[1]

x = numpy.arange(0, 30, .001)
x1 = [now + datetime.timedelta(diff) for diff in x]
y1 = [altitude(now + datetime.timedelta(diff)) for diff in x]
plt.plot(x1, y1)
plt.title('Plot of Moon Altitude vs. Time for Portland')
plt.xlabel('Time (days)')
plt.ylabel('Altitude (degrees)')
plt.show()