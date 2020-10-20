"""Main module."""
import serial
import haversine
from . import position

class GPS:
    def __init__(self, port):
        self.port = port
        self.ser = serial.Serial(port, baudrate=9600, timeout=0.5)
        self.nmea_msg = ""
        self.position = position.Position()
        self.start_position = self.get_current_location()
        self.distance =0

    def setup(self):
        pass

    def restart(self):
        pass

    def clean_string(self):
        self.nmea_msg = ""

    def get_latitude(self):
        self.clean_string()
        while "GPGGA" not in self.nmea_msg:
            self.nmea_msg = self.ser.readline().decode("utf-8", "ignore")
        self.position.update(self.nmea_msg)
        return self.position.get_latitude()

    def get_longitude(self):
        self.clean_string()
        while "GPGGA" not in self.nmea_msg:
            self.nmea_msg = self.ser.readline().decode("utf-8", "ignore")
        self.position.update(self.nmea_msg)
        return self.position.get_longitude()

    def get_altitude(self):
        self.clean_string()
        while "GPGGA" not in self.nmea_msg:
            self.nmea_msg = self.ser.readline().decode("utf-8", "ignore")
        self.position.update(self.nmea_msg)
        return self.position.get_altitude()

    def get_current_location(self):
        self.clean_string()
        while "GPGGA" not in self.nmea_msg:
            self.nmea_msg = self.ser.readline().decode("utf-8", "ignore")
        self.position.update(self.nmea_msg)
        return self.position.get_current_location()

    def get_current_time(self):
        self.clean_string()
        while "GPGGA" not in self.nmea_msg:
            self.nmea_msg = self.ser.readline().decode("utf-8", "ignore")
        self.position.update(self.nmea_msg)
        return self.position.get_current_time()

    def set_distination(self, latitude, longitude):
        self.distination = (latitude, longitude)

    def get_distance(self, latitude, longitude):
        self.set_distination(latitude, longitude)
        self.distance = haversine(self.get_current_location(), self.distination)
        return self.distance

    def get_speed(self):
        self.clean_string()
        while "GPVGT" in self.nmea_msg:
            msg = pynmea2.parse(nmea_msg)
            speed = msg.spd_over_grnd_kmph
        pass

    def get_time_of_arrival(self):
        #calculates travel_time in hours
        time = float(self.distance)/float(self.get_speed())*3600
        day = time // (24 * 3600)
        time = time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        
        #gettings arrival time and splitting into hours, minutes and seconds
        current_time = str(self.get_current_time())        
        c_hour = int(current_time[0,2])
        c_minutes =  int(current_time[2,4])
        c_seconds = int(current_time[4,6])

        #calculating aarival times
        a_hours = c_hour+hour
        a_minutes = c_minutes+minutes
        a_seconds = c_seconds+seconds

        arrival_time=("%d:%d:%d" % (a_hours, a_minutes, a_seconds))
        return arrival_time

        pass

    def get_time_of_arrival(self, latitude, longitude):
        #calculates travel_time in hours
        time = float(self.get_distance(latitude,longitude))/float(self.get_speed())*3600
        day = time // (24 * 3600)
        time = time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        
        #gettings arrival time and splitting into hours, minutes and seconds
        current_time = str(self.get_current_time())        
        c_hour = int(current_time[0,2])
        c_minutes =  int(current_time[2,4])
        c_seconds = int(current_time[4,6])

        #calculating arival times
        a_hours = c_hour+hour
        a_minutes = c_minutes+minutes
        a_seconds = c_seconds+seconds

        arrival_time=("%d:%d:%d" % (a_hours, a_minutes, a_seconds))
        return arrival_time
        pass
    
    #distance travelled since start of trip to end distination
    # distance stored is reset to zero after each trip
    def store_distance(self):
        self.distance = haversine(self.start_position, self.destination)
        return self.distance 
        pass

    def get_mileage(self, date1, date2):
        pass

        #current_position = self.get_current_location
        #current_latitude = float(current_position[0])
        #current_longitude = float(current_position[1])
        #destination_latitude = float(self.destination[0])
        #destination_longitude = float(self.destination[1])
