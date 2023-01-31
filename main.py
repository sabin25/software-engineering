

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  # slice
            "ham": 4,  # slice
            "cheese": 4,  # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  # slice
            "ham": 6,  # slice
            "cheese": 8,  # ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  # slice
            "ham": 8,  # slice
            "cheese": 12,  # ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  # slice
    "ham": 18,  # slice
    "cheese": 24,  # ounces
}


# Complete functions

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""

    # Make an instance of SandwichMachine class and write the rest of the codes

    # asking user for the input
    choice1 = "small"
    choice2 = "medium"
    choice3 = "large"
    choice4 = "off"
    choice5 = "report"

    choice = input("What would you like? (small / medium / large / off / report): ")

    if choice == choice1 or choice == choice2 or choice == choice3:
        print("You have selected a", choice, "sandwich")

    if choice == choice4:
        print("The machine is turned off")
        exit()
    if choice == choice5:
        print(resources)
        exit()
    else:
        print("Please insert coins.")

    largeDollar = int(input("how many large dollars?: "))
    halfDollar = int(input("how many half dollars?: "))
    quarters = int(input("how many quarters?: "))
    nickels = int(input("how many nickels?: "))

    totalPay = largeDollar + halfDollar + quarters + nickels
    print('You paid :$', totalPay)

    if choice == choice1 and totalPay > 1.75:
        change = totalPay - 1.75
        print("Your change is", change)
        print("your sandwich is ready. bon appetit!")
    else:
        print("please insert more money")

    if choice == choice2 and totalPay > 3.25:
        change = totalPay - 3.25
        print("Your change is", change)
        print("your sandwich is ready. bon appetit!")
    else:
        print("please insert more money")

    if choice == choice3 and totalPay > 5.5:
        change = totalPay - 5.5
        print("Your change is", change)
        print("your sandwich is ready. bon appetit!")
    else:
        print("please insert more money")

