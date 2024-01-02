print("Welcome to the tip calculator.")

total_cost=float(input("Please enter the total cost of your meal:"))

tip_per=int(input("What percentage tip would you like to give?\n 10,12,15?\n"))

tip_cal=(total_cost*tip_per)/100

split_in=int(input("How many people to split the bill?\n"))

final_bill=float((total_cost+tip_cal)/split_in)
print(f"Thank you visiting Your Final bill is {final_bill}")
