#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python


#greeting

print("--------------------------------------")
print("| Welcome to the Tip Calculator App! |")
print("--------------------------------------\n")

#Ask the user for the total bill amount and convert to a float

# total_bill = input("What was total bill? £")
bill = float(input("What was total bill? £"))

#Ask the user for the percentage tip they would like to give and convert it to a float
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

#Ask the user for the number of people to split the bill by and convert it to a float
people = int(input("How many people to split the bill? "))

#work out the tip %
tip_pc = tip / 100

#work out the tip amount
tip_amount = bill * tip_pc

#work out the bill including the tip
bill_inc_tip = bill + tip_amount

#work out the amount to pay per person and round it to 2 decimal places, and format the outout to display both digits after the decimal points
amt_per_person = bill_inc_tip / people
# final_amount = round(amt_per_person, 2)
final_amount = "{:.2f}".format(amt_per_person)

#format and print the output 

message = (f"Each person should pay: £{final_amount}")
print(message)