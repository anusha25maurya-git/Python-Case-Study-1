Python-CS-1
Grocery Store Billing System

Problem Statement=>

A grocery store wants to calculate the total cost of items purchased by a customer. 
The program should: 
1)Accept prices of 3 items from the user. 
2)Calculate the total cost. 
3)Apply a 10% discount if the total exceeds $50. 
4)Display the Original Total, Discount, and Final Payable Amount.

Approach=>

1)Take input for the prices of three items using input() and convert them to float. 
2)Calculate the total cost by adding all three prices. 
3)Check if the total cost is greater than 50: If yes, calculate a 10% discount. Otherwise, discount remains 0. 
4)Subtract the discount from the total cost to get the final amount. 
5)Display the results formatted to two decimal places.

Sample Output=> Enter the price of item1: 30 
                Enter the price of item2: 23 
                Enter the price of item3: 90

Original Total: $ 143.00 
Discount Total: $ 14.30 
Final Amount: $ 128.70


############################################################################################################################################################################

Python CS-2

Problem Statement=>

Build a Python program to simulate a Temperature Monitoring System for an assumed IoT environment.
The system should=>
1)Accept minimum and maximum temperature limits from the user.
2)Generate random temperature values at every 2-second interval.
3)Compare the generated temperature with the given limits.
4)Display appropriate status messages:
  Low Temperature Alert
  High Temperature Alert
  Normal Temperature

Approach=>

User Input=>
Take minimum and maximum temperature limits from the user.

Temperature Simulation=>
Use Python’s random module to generate random temperature values.
Generate values slightly beyond the given range to simulate real-world fluctuations.

Comparison Logic=>
If temperature < minimum limit → Display Low Temperature Alert
If temperature > maximum limit → Display High Temperature Alert
Otherwise → Display Temperature is Normal

Time Interval=>
Use time.sleep(2) to update the temperature every 2 seconds.

Continuous Monitoring=>
Use an infinite loop (while True) to simulate continuous IoT monitoring.


Sample Output=>
Enter minimum temperature limit: 20
Enter maximum temperature limit: 30

Current Temperature: 18
Low Temperature Alert!

Current Temperature: 25
Temperature is Normal

Current Temperature: 35
High Temperature Alert!

Current Temperature: 22
Temperature is Normal
