from datetime import datetime
import copy
import random

# Global list of transactions
transactions = []
history = []


# Function to create a bank transaction
def create_bank_transaction(day: int, amount_of_money: int, transaction_type: str, description: str):
    """
    Function to create a bank transaction.
    :param day: Day of the transaction (between 1 and 30).
    :param amount_of_money: Transaction amount (positive integer).
    :param transaction_type: Transaction type ('in' or 'out').
    :param description: Description of the transaction.
    :return: Dictionary representing the transaction.
    """
    if day < 1 or day > 30:
        raise ValueError("The day must be between 1 and 30.")
    if amount_of_money <= 0:
        raise ValueError("Amount of money must be positive.")
    if transaction_type not in ["in", "out"]:
        raise ValueError("The type must be either 'in' or 'out'.")
    return {
        "day": day,
        "amount_of_money": amount_of_money,
        "type": transaction_type,
        "description": description
    }


# (A) Add a transaction for the current day
def add_transaction(value: int, transaction_type: str, description: str):
    current_day = datetime.now().day  # Get the current day
    transaction = create_bank_transaction(current_day, value, transaction_type, description)
    transactions.append(transaction)
    print("Transaction added successfully!")


# (A) Insert a transaction for a specific day
def insert_transaction(day: int, value: int, transaction_type: str, description: str):
    transaction = create_bank_transaction(day, value, transaction_type, description)
    transactions.append(transaction)
    print("Transaction inserted successfully!")


# (B) Modify transactions
def remove_transaction_by_day(day: int):
    global transactions
    transactions = [t for t in transactions if t["day"] != day]
    print(f"All transactions from day {day} have been removed.")


def remove_transactions_by_day_range(start_day: int, end_day: int):
    global transactions
    transactions = [t for t in transactions if not (start_day <= t["day"] <= end_day)]
    print(f"Transactions from days {start_day} to {end_day} have been removed.")


def remove_transactions_by_type(transaction_type: str):
    global transactions
    transactions = [t for t in transactions if t["type"] != transaction_type]
    print(f"All '{transaction_type}' transactions have been removed.")


def replace_transaction(day: int, transaction_type: str, description: str, new_value: int):
    found = False
    for transaction in transactions:
        if transaction["day"] == day and transaction["type"] == transaction_type and transaction["description"] == description:
            transaction["amount_of_money"] = new_value
            found = True
            print(f"Transaction on day {day} with type '{transaction_type}' and description '{description}' has been replaced.")
            break
    if not found:
        print(f"No matching transaction found on day {day} with type '{transaction_type}' and description '{description}'.")


# (C) Display transactions
def display_transactions():
    if transactions:
        for transaction in transactions:
            print(f"Day: {transaction['day']}, Amount: {transaction['amount_of_money']}, Type: {transaction['type']}, Description: {transaction['description']}")
    else:
        print("No transactions to display.")


def display_transactions_by_type(transaction_type: str):
    filtered_transactions = [t for t in transactions if t["type"] == transaction_type]
    if filtered_transactions:
        for transaction in filtered_transactions:
            print(f"Day: {transaction['day']}, Amount: {transaction['amount_of_money']}, Type: {transaction['type']}, Description: {transaction['description']}")
    else:
        print(f"No {transaction_type} transactions to display.")


def display_transactions_by_amount(comparator: str, value: int):
    if comparator not in ['<', '>', '=']:
        print("Invalid comparator. Use '<', '>', or '='.")
        return
    if comparator == '<':
        filtered_transactions = [t for t in transactions if t["amount_of_money"] < value]
    elif comparator == '>':
        filtered_transactions = [t for t in transactions if t["amount_of_money"] > value]
    elif comparator == '=':
        filtered_transactions = [t for t in transactions if t["amount_of_money"] == value]

    if filtered_transactions:
        for transaction in filtered_transactions:
            print(f"Day: {transaction['day']}, Amount: {transaction['amount_of_money']}, Type: {transaction['type']}, Description: {transaction['description']}")
    else:
        print(f"No transactions found with amount {comparator} {value}.")


def compute_balance_at_day(target_day: int):
    balance = 0
    for transaction in transactions:
        if transaction["day"] <= target_day:
            if transaction["type"] == "in":
                balance += transaction["amount_of_money"]
            elif transaction["type"] == "out":
                balance -= transaction["amount_of_money"]
    return balance


def remove_transactions_by_type_and_less_than(transaction_type: str, amount: int):
    global transactions
    transactions = [t for t in transactions if not (t["type"] == transaction_type and t["amount_of_money"] < amount)]
    print(f"All '{transaction_type}' transactions with amount less than {amount} have been removed.")


# Function to save the current state to history
def save_to_history():
    global history
    history.append(copy.deepcopy(transactions))

# Undo functionality
def undo_last_action():
    global transactions, history
    if history:
        transactions = history.pop()  # Revert to the last saved state
        print("Last action undone.")
    else:
        print("No actions to undo.")