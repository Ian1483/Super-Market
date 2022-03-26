# Ian Depauw
# Super Market
# The if statements detect that a user has said yes
# Sources Used:
# https://www.delftstack.com/howto/python/if-with-string-in-python/

# Wallet
print("")
wallet = float(input("Enter money to spend, $"))

# Welcome Message
print("")
print("Welcome to the supermarket! We have a wide variety of groceries to purchase!")

# Fruit Sale
fruitSale = float(0.20)

# Fruit Prices
apple_P = (1 - fruitSale) * float(1.00)
banana_P = (1 - fruitSale) * float(1.50)

# Fruit Prompt
print("")
print("Are you looking at purchasing any fruit? ")
fruitPrompt = input(format(int(fruitSale * 100)) + "% off sale! ")
if fruitPrompt in ['y', 'Y', 'yes', 'Yes', 'YES']:

    # Enter Amount to Purchase
    print("")
    print("Enter the amount you want to purchase:")

    # Fruit Units
    apple = int(input("Apples, $" + format(apple_P, ".2f") + " "))
    banana = int(input("Bananas, $" + format(banana_P, ".2f") + " "))

    # Total Fruit Price
    print("")
    totalFruitPrice = (apple * apple_P) + (banana * banana_P)
    print("Total Fruit Cost: $", format(totalFruitPrice, ".2f"), sep='')
else:

    # If Customer Did Not Say Yes
    totalFruitPrice = float(0)

# Vegetable Sale
vegSale = float(0.30)

# Vegetable Prices
carrot_P = (1 - vegSale) * float(1.00)
broccoli_P = (1 - vegSale) * float(1.50)

# Vegetable Prompt
print("")
print("Are you looking at purchasing any vegetables? ")
vegPrompt = input(format(int(vegSale * 100)) + "% off sale! ")
if vegPrompt in ['y', 'Y', 'yes', 'Yes', 'YES']:

    # Enter Amount to Purchase
    print("")
    print("Enter the amount you want to purchase:")

    # Vegetable Units
    print("")
    carrot = int(input("Carrots, $" + format(carrot_P, ".2f") + " "))
    broccoli = int(input("Broccoli, $" + format(broccoli_P, ".2f") + " "))

    # Total Vegetable Price
    print("")
    totalVegPrice = (carrot * carrot_P) + (broccoli * broccoli_P)
    print("Total Vegetable Cost: $", format(totalVegPrice, ".2f"), sep='')
else:

    # If Customer Did Not Say Yes
    totalVegPrice = float(0)

# Total Cost
print("")
totalPrice = totalFruitPrice + totalVegPrice
print("Total Cost of Items: $", format(totalPrice, ".2f"), sep='')

# Purchase Success
if totalPrice == wallet or totalPrice > wallet:
    print("")
    print("Purchase Successful!")

# Purchase Failure
if totalPrice > wallet:
    print("")
    print("Purchase Failed!")

# Money Left Over
if not totalPrice > wallet:
    Balance = wallet - totalPrice
    print("Money Leftover: $", format(Balance, ".2f"), sep='')

# Exact Amount
if totalPrice == wallet:
    Balance = totalPrice - wallet
    print("No money leftover")

# Not Enough Money
if totalPrice > wallet:
    Balance = totalPrice - wallet
    print("Amount to be owed: $", format(Balance, ".2f"), sep='')