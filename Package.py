class Package:
    def __init__(self, packageID, street_address, city, state, zipcode, weight, deadline, currentStatus):
        self.packageID = packageID
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.weight = weight
        self.deadline = deadline
        self.currentStatus = currentStatus
        self.timeLeftHub = None
        self.arrivalTime = None

    def changeStatus(self, newStatus):
        self.currentStatus = newStatus


    def changeDeliveryTime(self, newTime):
        self.deliveryTime = newTime


    def __str__(self):
        return ("Package ID: %s, Street Address: %s, City: %s, State: %s Zipcode: %s Weight:%s Deadline: %s,  "
                "Current Status: %s, Time Left Hub: %s, Arrival Time: %s") % (
            self.packageID, self.street_address, self.city, self.state, self.zipcode, self.weight, self.deadline,
             self.currentStatus, self.timeLeftHub, self.arrivalTime)
