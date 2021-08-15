# As per the requirements:
# Marshall Christian 001520145


from datetime import timedelta
from DeliverySystem import PackageDelivery

(total_distance, packages_hash, packages) = PackageDelivery.run()

print('WGU Package Delivery System for C950 - Data Structures and Algorithms II')
print('Packages were delivered in {} miles'.format(total_distance))

while True:
    print()
    command = input("""\
Main Menu:
   1 - Look up based upon Package ID and a given time
   2 - View status of all packages for specific time - "HH:MM:SS"
   3 - Displays the total distance of all trucks traveled
   exit - Exit the program.
   Please enter a command: """)

    if command == '1':
        package_id = input('Please enter a package ID to lookup: ')

        # Lookup package ID from hash table
        # Time complexity: O(n) with being the size of the bucket
        package = packages_hash.find(int(package_id))

        time_string = input('Please enter a time in the format of HH:MM:SS : ')
        (hour, minute, sec) = time_string.split(':')
        timestamp = timedelta(hours=int(hour), minutes=int(minute), seconds=int(sec))

        print(package.report(timestamp))

    elif command == '2':
        time_string = input('Please enter a timestamp in HH:MM:SS format: ')
        (hour, minute, sec) = time_string.split(':')
        timestamp = timedelta(hours=int(hour), minutes=int(minute), seconds=int(sec))

        # Loop through packages and display their current status
        for package in packages:
            print(package.inline_report(timestamp))

    elif command == '3':
        print('Total Distance: {} miles'.format(total_distance))

    elif command == 'exit':
        exit()

    else:
        print('Invalid command. Please try again.')
