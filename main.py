# As per the requirements:
# Marshall Christian 001520145

# This project was created with the help of multiple CI's and the help of the WGU Discord server and WGU_CompSci Reddit thread.

from datetime import timedelta
from DeliverySystem import PackageDelivery


print("************************************************************************************************")
print("WGU Package Delivery System for C950 - Data Structures and Algorithms II by Marshall Christian")
print("************************************************************************************************")

(total_distance, packages_hash, packages) = PackageDelivery.run()

print("-----------------------------------------------------------------------------------------------------------------------")
print("Congrats! All packages were delivered on time and your shift is over. You can clock out knowing you did a great job! ")
print("-----------------------------------------------------------------------------------------------------------------------")
print('Packages were delivered in {} miles'.format(total_distance))




while True:

    # This is to help the special packages be displayed without repeated code
    def package_look_up_for_interface(package_id):
        package = packages_hash.look_up(int(package_id))
        package_time = "12:00:00"
        (hour, minute, sec) = package_time.split(':')
        timestamp = timedelta(hours=int(hour), minutes=int(minute), seconds=int(sec))
        print(package.specific_package_lookup(timestamp))

    print()
    user_input = input("""\
Main Menu:
   1 - Look up based upon Package ID and a given time
   2 - View status of all packages for specific time - "HH:MM:SS"
   3 - Displays the total distance of all trucks traveled
   4 - Displays all special packages in various categories
   exit - Exit the program.
   Please enter a number or "exit" to leave the program: """)

# Went with a simple if/else block for this since Python makes Switch/Case statements a pain.
    if user_input == "1":
        package_id = input("Please enter an ID of the package you wish to lookup ")

        # Lookup package ID from hash table
        # Time complexity: O(n) with being the size of the bucket
        package = packages_hash.look_up(int(package_id))

        package_time = input("Please enter a time in the format of HH:MM:SS : ")

        (hour, minute, sec) = package_time.split(':')
        timestamp = timedelta(hours=int(hour), minutes=int(minute), seconds=int(sec))

        print(package.specific_package_lookup(timestamp))

    elif user_input == "2":
        package_time = input("Please enter a time in the format of HH:MM:SS : ")
        (hour, minute, sec) = package_time.split(":")
        timestamp = timedelta(hours=int(hour), minutes=int(minute), seconds=int(sec))

        # Loop through packages and display their current status
        for package in packages:
            print(package.inline_report(timestamp))

    elif user_input == "3":
        print("Total Distance: {} miles".format(total_distance))

    elif user_input == "4":
        print("\n This will display all special packages.\n")

        print("All 10:30 deadline packages without other special notes:")

        package_look_up_for_interface(1)
        package_look_up_for_interface(29)
        package_look_up_for_interface(30)
        package_look_up_for_interface(31)
        package_look_up_for_interface(34)
        package_look_up_for_interface(37)
        package_look_up_for_interface(40)

        print("\nPackages to be delivered together: ")

        package_look_up_for_interface(13)
        package_look_up_for_interface(14)
        package_look_up_for_interface(15)
        package_look_up_for_interface(16)
        package_look_up_for_interface(19)
        package_look_up_for_interface(20)

        print("\nPackages delayed until 9:05 : ")

        package_look_up_for_interface(3)
        package_look_up_for_interface(18)
        package_look_up_for_interface(36)
        package_look_up_for_interface(38)

        print("\nWrong address updated and delivered after 10:20 : ")
        package_look_up_for_interface(9)


    elif user_input == "exit":
        exit()

    else:
        print("Invalid input. Please try again.")

