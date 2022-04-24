"""Super Market"""
__author__ = "Ian Depauw"
# The if statements detect that a user has said yes
# Sources Used:
# https://www.delftstack.com/howto/python/if-with-string-in-python/
# https://docs.python.org/3/tutorial/errors.html


def print_message():
    """
Welcomes the user to the supermarket
    """
    print("")
    print("Welcome to the supermarket!")
    print("We have a wide variety of groceries to purchase!")


def get_float_input():
    """
Asks the user how much money they have to spend
    """
    input_validation = True
    wallet = None
    while input_validation:
        try:
            print("")
            wallet = float(input("Enter money to spend in US dollars and cents"
                                 " $"))
            input_validation = False
        except ValueError:
            print("")
            print("Invalid Input! Please enter a number up to two decimal "
                  "places.")
    return wallet


def main():
    """
Main function
    """
    print_message()
    wallet = get_float_input()

    # Calculates the fruit sale
    fruit_sale = float(0.20)

    # Calculates the prices of the fruit with the sale
    apple_p = (1 - fruit_sale) * float(1.00)
    banana_p = (1 - fruit_sale) * float(1.50)

    # Prompts the user if they want to purchase any fruit
    print("")
    print("Are you looking at purchasing any fruit? ")
    fruit_prompt = input(format(int(fruit_sale * 100)) + "% off sale! ")
    if fruit_prompt in ['y', 'Y', 'yes', 'Yes', 'YES']:

        # Prompts the user how many of each fruit they want
        print("")
        print("Enter the amount you want to purchase:")

        # Tells the user how much each fruit costs and how much they want
        while True:
            try:
                apple = int(input("Apples per unit, $"
                                  + format(apple_p, ".2f") + " "))
                break
            except ValueError:
                print("Invalid Input! Please enter a whole number.")
        while True:
            try:
                banana = int(input("Bananas per unit, $"
                                   + format(banana_p, ".2f") + " "))
                break
            except ValueError:
                print("Invalid Input! Please enter a whole number.")

        # Tells the user the total cost of the fruit they have purchased
        print("")
        total_fruit_price = (apple * apple_p) + (banana * banana_p)
        print("Total Fruit Cost: $", format(total_fruit_price, ".2f"), sep='')
    elif fruit_prompt in ['n', 'N', 'no', 'No', 'NO']:

        # Sets the prices for all fruit to $0 if user said no
        total_fruit_price = float(0)
        apple = 0
        banana = 0
    else:

        # Sets the prices for all fruit to $0 if user didn't say yes or no
        print("Did not understand your response, taking it as a no.")
        total_fruit_price = float(0)
        apple = 0
        banana = 0

    # Tells the user the current items in their cart
    print("")
    print("Total Items In Cart:")

    # Shows how many apples are in the user's cart
    apple_cart = 0
    while apple_cart < apple:
        print("Apple")
        apple_cart += 1

    # Shows how many bananas are in the user's cart
    banana_cart = 0
    while banana_cart < banana:
        print("Banana")
        banana_cart += 1

    # Calculates the vegetable sale
    veg_sale = float(0.30)

    # Calculates the prices of the vegetables with the sale
    carrot_p = (1 - veg_sale) * float(1.00)
    broccoli_p = (1 - veg_sale) * float(1.50)

    # Prompts the user if they want to purchase any vegetables
    print("")
    print("Are you looking at purchasing any vegetables? ")
    veg_prompt = input(format(int(veg_sale * 100)) + "% off sale! ")
    if veg_prompt in ['y', 'Y', 'yes', 'Yes', 'YES']:

        # Prompts the user how many of each vegetable they want
        print("")
        print("Enter the amount you want to purchase:")

        # Tells the user how much each vegetable costs and how much they want
        while True:
            try:
                carrot = int(input("Apples per unit, $"
                                   + format(carrot_p, ".2f") + " "))
                break
            except ValueError:
                print("Invalid Input! Please enter a whole number.")
        while True:
            try:
                broccoli = int(input("Bananas per unit, $"
                                     + format(broccoli_p, ".2f") + " "))
                break
            except ValueError:
                print("Invalid Input! Please enter a whole number.")

        # Tells the user the total cost of the vegetables they have purchased
        print("")
        total_veg_price = (carrot * carrot_p) + (broccoli * broccoli_p)
        print("Total Vegetable Cost: $", format(total_veg_price, ".2f"),
              sep='')
    elif veg_prompt in ['n', 'N', 'no', 'No', 'NO']:

        # Sets the prices for all vegetables to $0 if user said no
        total_veg_price = float(0)
        carrot = 0
        broccoli = 0
    else:

        # Sets the prices for all vegetables to $0 if user didn't say yes or no
        print("Did not understand your response, taking it as a no.")
        total_veg_price = float(0)
        carrot = 0
        broccoli = 0

    # Tells the user the current items in their cart
    print("")
    print("Total Items In Cart:")

    # Shows how many apples are in the user's cart
    apple_cart = 0
    while apple_cart < apple:
        print("Apple")
        apple_cart += 1

    # Shows how many bananas are in the user's cart
    banana_cart = 0
    while banana_cart < banana:
        print("Banana")
        banana_cart += 1

    # Shows how many carrots are in the user's cart
    carrot_cart = 0
    while carrot_cart < carrot:
        print("Carrot")
        carrot_cart += 1

    # Shows how much broccoli are in the user's cart
    broccoli_cart = 0
    while broccoli_cart < broccoli:
        print("Broccoli")
        broccoli_cart += 1

    # Tells the user the total cost of all their purchased items
    total_price = total_fruit_price + total_veg_price
    print("")
    print("Total Cost of Items: $", format(total_price, ".2f"), sep='')

    # Displays 50 dashes above the purchase success or failure
    for x in range(50):
        print("-", end="")

    # Tells the user if their purchase was successful
    if total_price == wallet or total_price < wallet:
        print("")
        print("Purchase Successful!")

    # Tells the user if their purchase failed
    if total_price > wallet:
        print("")
        print("Purchase Failed!")

    # Tells the user if they do not have any money leftover
    if not total_price != wallet and total_price == wallet:
        print("No money leftover")

    # Tells the user if they have money leftover
    if total_price < wallet:
        balance = wallet - total_price
        print("Money Leftover: $", format(balance, ".2f"), sep='')

    # Tells the user if they have money to be owed
    if total_price > wallet:
        balance = total_price - wallet
        print("Amount to be owed: $", format(balance, ".2f"), sep='')

    # Displays 50 dashes below the money leftover or to be owed
    print("-" * 50)


# Call to main
main()
