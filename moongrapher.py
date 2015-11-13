from luna import *
import datetime
import matplotlib.pyplot as plt
import numpy

now = datetime.datetime.now()

def altitude(latitude, longitude, date, tz):
    home = Luna(latitude, longitude)
    date = date - datetime.timedelta(hours=tz)
    return home.calculate(date.year, date.month, date.day,
                          date.hour, date.minute, date.second)[1]

def azimuth(latitude, longitude, date, tz):
    home = Luna(latitude, longitude)
    date = date - datetime.timedelta(hours=tz)
    return home.calculate(date.year, date.month, date.day,
                          date.hour, date.minute, date.second)[0]

def graphAltitude(latitude, longitude, tz, days, locationString):
    x = numpy.arange(0, days, .001)
    x1 = [now + datetime.timedelta(diff) for diff in x]
    y1 = [altitude(latitude, longitude, now + datetime.timedelta(diff), tz) for diff in x]
    plt.plot(x1, y1)
    plt.title('Plot of Moon Altitude vs. Time for {}'.format(locationString))
    plt.xlabel('Date')
    plt.ylabel('Altitude (degrees)')
    plt.show()

def graphAzimuth(latitude, longitude, tz, days, locationString):
    x = numpy.arange(0, days, .001)
    x1 = [now + datetime.timedelta(diff) for diff in x]
    y1 = [azimuth(latitude, longitude, now + datetime.timedelta(diff), tz) for diff in x]
    plt.plot(x1, y1)
    plt.title('Plot of Moon Azimuth vs. Time for {}'.format(locationString))
    plt.xlabel('Date')
    plt.ylabel('Azimuth (degrees)')
    plt.show()

graphAltitude(45.523318, -122.679093, -8, 60, "Portland, OR")