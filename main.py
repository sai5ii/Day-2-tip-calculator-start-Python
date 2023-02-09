#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
totalBill = input("What was the total Bill? $")
percentTip= input("What percentage tip would you like to give? 10, 12 or 15? ")
numPeople= input("How many people to split the bill? ")
eachPays = (float(totalBill)/int(numPeople)) * ((float(percentTip)+100)/100)
billperPerson = "{:.2f}".format(eachPays)

print(f"Each person should pay: $ {billperPerson}")
