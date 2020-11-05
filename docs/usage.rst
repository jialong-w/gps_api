=====
Usage
=====

To use GPS API in a project::

  # import the package
  import gps_api

  # instantiate the GPS object with the port name on your device
  # to which the GPS module is connected
  GPS = gps_api.GPS(port)
  # get current location
  location =  GPS.get_current_location()
