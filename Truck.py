class Truck:

    def __init__(self, number, current_location, departure_time, distance_traveled, all_packages,
                 max_num_package, speed, current_time, packages_delivered):
        self.number = number
        self.current_location = current_location
        self.departure_time = departure_time
        self.distance_traveled = distance_traveled
        self.all_packages = all_packages
        self.max_num_package = max_num_package
        self.speed = speed
        self.current_time = current_time
        self.packages_delivered = packages_delivered

        # Overwriting the string method so that it does not return an object reference
    def __str__(self):
        return "Truck Number: %s, Current Location: %s, Departure Time: %s, Distance Traveled: %s, All Packages: %s, Maximum Number of Packages: %s, Speed: %s, Current Time: %s, Packages Delivered: %s" % (
            self.number, self.current_location, self.departure_time, self.distance_traveled,
            self.all_packages, self.max_num_package, self.speed, self.current_time, self.packages_delivered)
