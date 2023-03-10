### Data ###

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


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            # print(item, ingredients[item])
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        total = int(input("how many large dollars?: ")) * 1
        total += int(input("how many half dollars?: ")) * 0.5
        total += int(input("how many quarters?: ")) * 0.25
        total += int(input("how many nickels?: ")) * 0.05
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")


# a = SandwichMachine(resources)
# a.check_resources({"bread": 12, "ham": 18, "cheese": 24})
### Make an instance of SandwichMachine class and write the rest of the codes ###
is_on = True

sandwich_maker = SandwichMachine(resources)

while is_on:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Bread: {resources['bread']} slice(s)")
        print(f"Ham: {resources['ham']} slice(s)")
        print(f"Cheese: {resources['cheese']} pound(s)")
    else:
        sandwich = recipes[choice]
    #     sandwich = {
    #     "ingredients": {
    #         "bread": 2,  ## slice
    #         "ham": 4,  ## slice
    #         "cheese": 4,  ## ounces
    #     },
    #     "cost": 1.75,
    # }
        if sandwich_maker.check_resources(sandwich["ingredients"]):
            payment = sandwich_maker.process_coins()
            if sandwich_maker.transaction_result(payment, sandwich["cost"]):
                sandwich_maker.make_sandwich(choice, sandwich["ingredients"])