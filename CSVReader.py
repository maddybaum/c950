# Sources used: WGUPS Project Implementation Steps document, Webinar 2 Getting Greedy, Who Moved My Data
# Class to support reading the 3 attached csv files

import csv

from Hashtable_Chaining import Hashtable_Chaining
from Package import Package


# Per instructions from WGUPS Project Implementation Steps suggests a loadPackageData(Hashtable) method to read data from package CSV
def loadPackageData(file_name, packageTable):
    with open(file_name) as package_file:
        packages = csv.reader(package_file, delimiter=',')
        for package in packages:
            pID = int(package[0])
            pStreet = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pStatus = "Ready to load on truck"
            p = Package(pID, pStreet, pCity, pState, pZip, pWeight, pDeadline, pStatus)
            packageTable.insert(pID, p)



# Per instructions from WGUPS Project Implementation Steps
# There is a suggestion to create loadDistanceData to read distanceCSV file row by row
def loadDistanceData(file_name, distance_list):
    # Open the file
    with open(file_name) as distance_file:
        # Read the file with using a comma as a separateor
        distances = csv.reader(distance_file, delimiter=',')
        for distance in distances:
            # Add each distance to the distance list used as the second parameter
            distance_list.append(distance)


def loadAddressData(file_name, address_list):
    # Open the file
    with open(file_name) as address_file:
        # Split up how the file is read by where there is a comma
        addresses = csv.reader(address_file, delimiter=',')
        # For each address in the file, append it to the address_list that is used as the second parameter
        for address in addresses:
            address_list.append(address)
