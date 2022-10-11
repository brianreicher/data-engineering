from account import *


def main():
    account = Account(500.00)
    account.deposit(25.0)

    try:
        account.withdraw(200.0)
    except AssertionError as ae:
        print(str(ae))
    except TypeError as te:
        print(str(te))

    print(account.balance)


if __name__ == '__main__':
    main()
