import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    sandwich_size = input("What would you like ? small / medium / large: ")
    extra_ingredients = recipes[sandwich_size]["ingredients"]
    if sandwich_maker_instance.check_resources(extra_ingredients):
        cost = recipes[sandwich_size]["cost"]
        print("The total cost for your order is: $", cost)
        coins = cashier_instance.process_coins()
        if cashier_instance.transaction_result(coins, cost):
            sandwich_maker_instance.make_sandwich(sandwich_size, extra_ingredients)
            print("Your sandwich is ready. Bon Appetit!")
        else:
            print("Not enough funds. Please insert more money")
    else:
        print("The machine is out of ingredients.")


if __name__ == "__main__":
    main()


