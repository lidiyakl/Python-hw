# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


def add_money(balance, transactions):
    while True:
        try:
            amount = int(input("Введите сумму для пополнения (кратную 50): "))
            if amount % 50 == 0 and amount > 0:
                balance += amount
                transactions.append(f"Пополнение: +{amount:.2f}")
                return balance
            else:
                print("Введена некорректная сумма (не кратна 50)")
        except ValueError:
            print('Введите корректное число.')


def withdrawal_money(balance, transactions):
    while True:
        try:
            amount = int(input("Введите сумму для снятия (кратную 50): "))
            if amount % 50 == 0 and amount > 0:
                commission = min(max(30, amount * 0.015), 600)
                if amount + commission <= balance:
                    balance -= (amount + commission)
                    transactions.append(f"Снятие: -{amount:.2f}, комиссия: -{commission:.2f}")
                    return balance
                else:
                    print("Недостаточно средств на счете.")
                    return balance
            else:
                print("Введена некорректная сумма (не кратна 50)")
        except ValueError:
            print("Введите корректное число.")


def tax_money(balance, transactions):
    if balance > 5_000_000:
        print("С вас сняли налог на богатство:", balance * 0.1)
        tax = balance * 0.1
        balance = balance - tax
        transactions.append(f"Налог: -{tax:.2f}")
    return balance


def bonus_money(balance, transactions):
    bonus = balance * 0.03
    new_balance = balance + bonus
    transactions.append(f"Бонус: +{bonus:.2f}")
    print(f"Начислен бонус 3%: {bonus:.2f} у.е.")
    return new_balance


def print_history(data: list):
    if data:
        print("История операций: ")
        for i in data:
            print(i)
        print()
    else:
        print("История операций пуста.")
        print()


def atm_simulation():
    balance = 0.00
    transactions = []
    count = 0

    while True:
        tax_money(balance, transactions)

        print(f"Текущий баланс: {balance:.2f} у.е.")
        print("1. Пополнить счет")
        print("2. Снять средства")
        print("3. Просмотр истории операций")
        print("0. Выйти")

        action = input("Выберите действие: ")

        match action:
            case "1":
                balance = add_money(balance, transactions)
                count += 1
                if count % 3 == 0:
                    balance = bonus_money(balance, transactions)
            case "2":
                balance = withdrawal_money(balance, transactions)
                count += 1
                if count % 3 == 0:
                    balance = bonus_money(balance, transactions)
            case "3":
                print_history(transactions)
            case "0":
                print("Завершаем работу банкомата.")
                exit()
            case _:
                print("Введите корректное число.")


if __name__ == "__main__":
    atm_simulation()