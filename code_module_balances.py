# Import code module
import code

bal_a = 2324
bal_b = 0
bal_c = 409
bal_d = -2

account_balances = [bal_a, bal_b, bal_c, bal_d]


def display_bal():
    for balance in account_balances:
        if balance < 0:
            print("Account balance of {} is below 0; add funds now."
                  .format(balance))

        elif balance == 0:
            print("Account balance of {} is equal to 0; add funds soon."
                  .format(balance))

        else:
            print("Account balance of {} is above 0.".format(balance))

# Use interact() function to start the interpreter with local namespace
code.interact(banner="Start", local=locals())

display_bal()
