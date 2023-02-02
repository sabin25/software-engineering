recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}
# Complete functions ###

class SandwichMachine:
    def __init__(self, machine_resources):
        """Receives resources as input.
        Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""

        for foodSrc, qty in ingredients.items():
            if self.machine_resources.get(foodSrc) is None or self.machine_resources[foodSrc] < qty:
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
        Hint: include input() function here, e.g. input("how many quarters?: ")"""
        coins = {'large dollar': 1,
                 'half dollar': 1,
                 'quarter': 1,
                 'nickel': 1}
        subTotal = 0
        for coin in coins:
            try:
                amount = int(input(f'Insert {coin}: '))
                subTotal += amount * coins[coin]
            except ValueError:
                pass
        return subTotal

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
         Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            return False
        else:
            change = coins - cost
            if change > 0:
                print(f'your change is ${change}')
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
         Hint: no output"""
        for foodSrc, qty in order_ingredients.items():
            self.machine_resources[foodSrc] -= qty

# Make an instance of SandwichMachine class and write the rest of the codes ###

sandwichMaker = SandwichMachine(resources)

while True:
    print("What would you like? (small/ medium/ large/ off/ report)")
    userChoice = input().lower()

    # users choose small sandwich
    if userChoice == "small":
        order_ingredients = recipes[userChoice]["ingredients"]
        cost = recipes[userChoice]["cost"]
        if sandwichMaker.check_resources(order_ingredients):
            coins = sandwichMaker.process_coins()
            if sandwichMaker.transaction_result(coins, cost):
                sandwichMaker.make_sandwich(userChoice, order_ingredients)
                print(f'{userChoice} sandwich is ready. bon appetit')
        else:
            print("not enough ingredients")
    elif userChoice == "off":
        print("the machine is off")
    elif userChoice == "report":
        for foodSrc, qty in sandwichMaker.machine_resources.items():
            print(f'{foodSrc}: {qty}')

    # users choose medium sandwich
    if userChoice == "medium":
        order_ingredients = recipes[userChoice]["ingredients"]
        cost = recipes[userChoice]["cost"]
        if sandwichMaker.check_resources(order_ingredients):
            coins = sandwichMaker.process_coins()
            if sandwichMaker.transaction_result(coins, cost):
                sandwichMaker.make_sandwich(userChoice, order_ingredients)
                print(f'{userChoice} sandwich is ready. bon appetit')
        else:
            print("not enough ingredients")
    elif userChoice == "off":
        print(" ")
    elif userChoice == "report":
        for foodSrc, qty in sandwichMaker.machine_resources.items():
            print(f'{foodSrc}: {qty}')

    # users choose large sandwich
    if userChoice in ["large", "LARGE"]:
        order_ingredients = recipes[userChoice]["ingredients"]
        cost = recipes[userChoice]["cost"]
        if sandwichMaker.check_resources(order_ingredients):
            coins = sandwichMaker.process_coins()
            if sandwichMaker.transaction_result(coins, cost):
                sandwichMaker.make_sandwich(userChoice, order_ingredients)
                print(f'{userChoice} sandwich is ready. bon appetit')
        else:
            print("not enough ingredients")
    elif userChoice == "off":
        print(" ")
    elif userChoice == "report":
        for foodSrc, qty in sandwichMaker.machine_resources.items():
            print(f'{foodSrc}: {qty}')

