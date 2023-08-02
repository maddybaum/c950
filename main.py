# Madeline Baum 010476624
# Written with Python 3.9

import csv

from Hashtable_Chaining import Hashtable_Chaining
from datetime import datetime
import datetime
import Truck
import Package
import CSVReader

# Create a variable called packageTable that is a hashtable from the Hashtable_Chaining class
packageTable = Hashtable_Chaining()

# This is a method to search for the text address and find the ID of that address
def getAddressNum(streetAddress):
    # Open the file
    with open("Addresses.csv") as address_file:
        addresses = csv.reader(address_file, delimiter=',')
        for address in addresses:
            # Matches street address text found in index 2 to the address ID found in index 0
            if streetAddress in address[2]:
                # Return the ID which is found in index 0
                return int(address[0])


# I used this Stack Overflow post to get help with finding the distance in a specific cell (How Can I Get a Specific Field of a CSV File?). Please see Task 2 Write Up for full citation
def addressDistance(address1ID, address2ID):
    # Open the distances.csv
    with open("Distances.csv") as distances:
        distanceCSV = csv.reader(distances)
        distanceCSV = list(distanceCSV)
        # Set distance = to the ID of address1 going horizontally and ID of address2 going vertically
        distance = distanceCSV[address1ID][address2ID]
        # Initially I did not include the portion below and was running into bugs due some cells having no data
        if distance == '' or distance == None:
            # If the above doesn't work then switch the order of the address IDs to get the distance
            distance = distanceCSV[address2ID][address1ID]
            # Return the distance found in the CSV
        return float(distance)


# All trucks will be starting at the package hub, have a maximum capacity of 16 and a speed of 18mph
# Determine packages that will be on first truck
firstTruckPackages = [1, 2, 13, 14, 15, 16, 19, 20, 21, 29, 30, 39, 40, 10, 34, 37]
# Create firstTruck object and determine all attributes
# firstTruck leaves right when the day begins at 8AM
# Turn the times into times instead of strings
firstTruck = Truck.Truck(1, "4001 South 700 East", datetime.timedelta(hours=8, minutes=0), 0, firstTruckPackages, 16,
                         18, datetime.timedelta(hours=8, minutes=0), [])
# Decide which packages will be on truck 2
secondTruckPackages = [3, 5, 6, 12, 17, 18, 22, 25, 26, 28, 31, 32, 36, 38]
# Create secondTruck object and determine all attributes
# Second truck waits until 9:05 for the packages that are delayed on flight
secondTruck = Truck.Truck(2, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5), 0, secondTruckPackages, 16,
                          18, datetime.timedelta(hours=9, minutes=5), [])
# Decide which packages will be on truck 3
# Third truck waits until 10:30 when the correct address can be assigned to package 9
thirdTruckPackages = [8, 9, 11, 23, 24, 27, 33, 35, 4, 7]
# Create thirdTruck object and determine attributes
thirdTruck = Truck.Truck(3, "4001 South 700 East", datetime.timedelta(hours=10, minutes=20), 0, thirdTruckPackages, 16,
                         18, datetime.timedelta(hours=10, minutes=20), [])


def beginRoute(truck):
    # We will manually load the packages on truck by starting with an empty array
    onTruck = []
    # For each package on the truck, look up the package ID, and add the corresponding package object to the onTruck list
    for ID in truck.all_packages:
        # Search will return the whole package object
        individualPackage = packageTable.search(ID)
        onTruck.append(individualPackage)
        # Set the truck's packages to the list of package objects instead of just the IDs

    # While the number of packages on the truck is greater than 0
    while len(onTruck) > 0:
        # Use dummy value of 1000 because no addresses are actually that far away. If we used 0 then no address would be closer, so need to use a number that is too big
        nextDestinationDistance = 1000
        # Next package will be empty object until reassigned
        # Address of the next package is an empty string until reassigned
        # For each item in the list onTruck
        for item in onTruck:
            # The item's ID is found by looking up the street address string using method above
            addressID = getAddressNum(str(item.street_address))
            # If the distance between those two address (current location and item in the list) is less than the value held in nextDestinationDistance, then reassign nextDestinationDistance to the new lower value
            # Set the next package to deliver to be the one that is currently the closest, if a new package is closer then set the variable ot the new closer package
            if addressDistance(getAddressNum(truck.current_location), addressID) <= nextDestinationDistance:
                nextDestinationDistance = addressDistance(getAddressNum(truck.current_location),
                                                          getAddressNum(item.street_address))
                nextPackageToDeliver = item
                # Continue to iterate through the list
        # Remove the package that was delivered
        onTruck.remove(nextPackageToDeliver)
        # Add the distance that package was from the previous location to the truck's total distance traveled
        truck.distance_traveled += nextDestinationDistance
        # Calculate the time in minutes to travel the distance to the next destination at 18MPH
        timeInMinutes = 60 / 18 * float(nextDestinationDistance)
        # Add the time in minutes to the current time to get the new time
        # I received help from my CI who suggested using datetime.timedelta for dealing with times
        truck.current_time += datetime.timedelta(minutes=timeInMinutes)
        # Set the package arrival time to the current time
        nextPackageToDeliver.arrivalTime = truck.current_time
        # Set the time the package left the hub to the time that the truck it rode on left the hub
        nextPackageToDeliver.timeLeftHub = truck.departure_time
        # Now that the truck has traveled, its new current location is where it is dropping off the pacakge
        truck.current_location = nextPackageToDeliver.street_address
        # Now the truck has delivered this package
        if len(onTruck) == 0:
            currentLocationID = getAddressNum(truck.current_location)
            distanceBackToHub = addressDistance(currentLocationID, 0)
            truck.distance_traveled += distanceBackToHub
        truck.packages_delivered.append(nextPackageToDeliver)
        nextPackageToDeliver.departure_time = truck.departure_time


# Include format example for time input
def main():
    print("Hello and welcome to WGUPS' new order tracking system!")
    print("First, let's talk about some of the business requirements. Each truck has a maximum capacity of 16 packages and leaves at a different time.")
    print("Truck 1 starts off with", len(firstTruck.all_packages), "packages. This truck leaves at", firstTruck.departure_time)
    print("Truck 2 starts off with", len(secondTruck.all_packages), "packages. This truck leaves at", secondTruck.departure_time)
    print("Truck 3 starts off with", len(thirdTruck.all_packages), "packages. This truck leaves at", thirdTruck.departure_time)


    distanceList = []
    addressList = []

    # Load package data from CSV file into packageTable hashtable
    CSVReader.loadPackageData("Packages.csv", packageTable)
    CSVReader.loadDistanceData("Distances.csv", distanceList)
    CSVReader.loadAddressData("Addresses.csv", addressList)

    beginRoute(firstTruck)
    beginRoute(secondTruck)
    beginRoute(thirdTruck)
    distanceTotal = firstTruck.distance_traveled + secondTruck.distance_traveled + thirdTruck.distance_traveled
    print("The total distance traveled between all three trucks is", distanceTotal, "miles")
    print("Please enter a time when you would like to view package status. Please use the format HH:MM:SS")
    inputTime = input()
    (h, m, s) = inputTime.split(":")
    inputTimeDelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    print("If you would like to view only one package at", inputTime, "please press 1", "If you would like to view all packages at ", inputTime, " please press 2")
    inputChoice = int(input())
    if inputChoice == 1:
        print("Please type the package ID number for the package you would like to track. (For example type 3)")
        packageToViewID = int(input())
        packageToView = packageTable.search(packageToViewID)
        print(packageToView, "are the general details")
        if(inputTimeDelta > packageToView.arrivalTime):
            print("The package was delivered by", inputTime, ". It was delivered at", packageToView.arrivalTime)
        else:
            print("The package was not delivered yet by", inputTime, ". It will be delivered at", packageToView.arrivalTime)
    elif inputChoice == 2:
        print("Printing all package data for", inputTime)
        for packageID in range(1, 41):
            item = packageTable.search(packageID)
            if item.arrivalTime < inputTimeDelta:
                item.currentStatus = "Delivered!"
                print(item)
                print(item.packageID, "was delivered by this time.")
            elif item.timeLeftHub > inputTimeDelta:
                item.currentStatus = "At the hub"
                print(item)
                print(item.packageID, "hasn't left the hub yet")
            else:
                item.currentStatus = "En Route"
                print(item)
                print(item.packageID, "was not delivered by this time.")
    else:
        print("Cannot interpret input. Please try again")
        exit()
if __name__ == "__main__":
    main()
