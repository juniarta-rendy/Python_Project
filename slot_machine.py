import random
import numpy as np

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}

symbols_value = {
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2
}

def check_winning(columns, lines, bet, values):
    winning = 0
    win_round = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            value_to_check = column[line]
            if symbol != value_to_check:
                break
        else:
            winning += bet * values[symbol]
            win_round.append(line+1)
    return winning, win_round


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            column.append(value)
            current_symbols.remove(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row])
        


def deposit():
    while True:
        amount = input('How much you want to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0')
        else:
            print('Please Enter Number')
    return amount

def get_number_lines():
    while True:
        lines = input('How many rounds you want to play (1-' +str(MAX_LINES) +')?')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f'Rounds must between 1- {MAX_LINES}')
        else:
            print('Please Enter Number')
    return lines

def get_bet():
    while True:
        bet = input('How much you want bet on each round? $')
        if bet.isdigit():
            bet = int(bet)
            if bet > 0:
                break
            else:
                print(f'Bet must between {MIN_BET} - {MAX_BET}')
        else:
            print('Please Enter Number')
    return bet

def game(balance):
    lines = get_number_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f'Not enough balance. Your Current balance is ${balance}')
            dep = input('Do you want to deposit? y/n: ').lower()
            if dep == 'y':
                balance += deposit()
        else:
            print(f'You are betting {bet} on {lines} rounds. Total bet: ${total_bet}')
            break
            
    slots = get_slot_machine_spin(ROWS,COLS,symbols)
    print_slot_machine(slots)
    winnings ,win_rounds = check_winning(slots,lines,bet,symbols_value)
    if len(win_rounds) > 0:
        print(f'You won on lines:', *win_rounds)
        if winnings < total_bet:
            print(f'You lose ${total_bet-winnings}')
        else:
            print(f'You Win ${winnings-total_bet}')
        balance += winnings-total_bet
        print(f'Total Balance: ${balance}')
    else:
        print(f'You Lose ${total_bet}')
        balance -= total_bet
        print(f'Total Balance: ${balance}')
    return balance

def main():
    balance = deposit()
    while True:
        print(f'Your current Balance ${balance}')
        spin = input("Enter to play (q to quit)").lower()
        if spin == 'q':
            break
        balance = game(balance)

    print(f'You left with ${balance}')
main()

    