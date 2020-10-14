# position.py

import pynmea2
import serial

class Position:
    """ position class, used to store latitude, longitude and altitude.
        get_latitude, get_longitude and get_current_location methods
    """

    def __init__(self, nmea_msg):
        if "GPGGA" in nmea_msg:
            msg = pynmea2.parse(nmea_msg)
            self.latitude = msg.latitude
            self.longitude = msg.longitude
            self.altitude = msg.altitude

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def get_altitude(self):
        return self.altitude

    def get_current_location(self):
        location = ""
        location = location + str(self.latitude) + " N " + str(self.longitude) + " W"
        return location
