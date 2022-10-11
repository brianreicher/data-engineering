from account import *


def main():
    account = Account(500.00)
    account.deposit(25.0)

    try:
        account.withdraw(1000.0)
    except InsufficientFunds as if_error:
        print(str(if_error))
        print(f'Overdrawn amount: ${if_error.overage()}')
    except AssertionError as ae:
        print(str(ae))
    except TypeError as te:
        print(str(te))
    else:
        print('Code running if no exception occurs')
    finally:
        print('Finally clause ALWAYS runs')
    print(f'Account balance: ${account.balance}')


if __name__ == '__main__':
    main()
