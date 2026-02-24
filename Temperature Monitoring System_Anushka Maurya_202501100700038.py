#TEMPERATURE MONITORING SYSTEM
import random
import time

min_temp= int(input("Enter minimum temperature limit: "))
max_temp = int(input("Enter maximum temperature limit: "))


while True:
    # Generate random temperature (simulating IoT sensor)
    temp = random.randint(min_temp-10, max_temp+10)

    print("Current Temperature:", temp)

    # Compare with limits
    if temp < min_temp:
        print("Low Temperature Alert!\n")
    elif temp > max_temp:
        print("High Temperature Alert!\n")
    else:
        print("Temperature is Normal\n")

    time.sleep(2)
