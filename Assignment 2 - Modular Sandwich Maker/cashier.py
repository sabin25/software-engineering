class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollar = int(input("How many one dollar? : "))
        quarters = int(input("How many quarters?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        return dollar * 1 + quarters * 0.25 + nickles * 0.05 + pennies * 0.01

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            return True
        return False
