from tema6 import *
import random



def generate_random_transactions():
    global transactions
    descriptions = [
        "Groceries", "Salary", "Electric bill", "Gym membership",
        "Online shopping", "Loan repayment", "Coffee shop",
        "Dining out", "Insurance payment", "Gift"
    ]
    transaction_types = ["in", "out"]

    for _ in range(10):
        day = random.randint(1, 30)  # Random day between 1 and 30
        amount_of_money = random.randint(10, 1000)  # Random amount between 10 and 1000
        transaction_type = random.choice(transaction_types)  # Random type: 'in' or 'out'
        description = random.choice(descriptions)  # Random description from the list
        transaction = create_bank_transaction(day, amount_of_money, transaction_type, description)
        transactions.append(transaction)


generate_random_transactions()


def a(n):
    cuv = n.split(' ')
    try:
        if cuv[0] == "add":
            save_to_history()  # Save state before adding
            value = int(cuv[1])
            transaction_type = cuv[2]
            description = ' '.join(cuv[3:])
            add_transaction(value, transaction_type, description)
        elif cuv[0] == "insert":
            save_to_history()  # Save state before inserting
            day = int(cuv[1])
            value = int(cuv[2])
            transaction_type = cuv[3]
            description = ' '.join(cuv[4:])
            insert_transaction(day, value, transaction_type, description)
        else:
            raise ValueError("Invalid command.")
    except ValueError as e:
        print(f"Error: {e}")

def b(n):
    cuv = n.split(' ')
    save_to_history()  # Save state before making changes
    if cuv[0] == "remove":
        if len(cuv) == 2 and cuv[1].isdigit():
            remove_transaction_by_day(int(cuv[1]))
        elif len(cuv) == 4 and cuv[2] == "to":
            remove_transactions_by_day_range(int(cuv[1]), int(cuv[3]))
        elif len(cuv) == 2:
            remove_transactions_by_type(cuv[1])
    elif cuv[0] == "replace":
        replace_transaction(int(cuv[1]), cuv[2], cuv[3], int(cuv[5]))

def c(n):
    cuv = n.split(' ')
    if len(cuv) == 1:
        display_transactions()
    elif cuv[1] == "in" or cuv[1] == "out":
        display_transactions_by_type(cuv[1])
    elif cuv[1] in ['<', '>', '=']:
        display_transactions_by_amount(cuv[1], int(cuv[2]))
    elif cuv[1] == "balance":
        print(f"Balance at day {cuv[2]}: {compute_balance_at_day(int(cuv[2]))}")

def d(n):
    cuv = n.split(' ')
    save_to_history()  # Save state before removing based on conditions
    if len(cuv) == 2:
        remove_transactions_by_type(cuv[1])
    elif len(cuv) == 3:
        remove_transactions_by_type_and_less_than(cuv[1], int(cuv[2]))
