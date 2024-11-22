class Category:
    def __init__(self, name):
        self.name = name
        self.income = 0.0
        self.expense = 0.0
        self.balance = 0.0
        self.ledger = []

    def __str__(self):
        str_category = self.name.center(30, '*')
        # l_name = len(self.name
        for entry in self.ledger:
            str_amount = str(float(entry['amount']))

            # 2 decimal
            if str_amount.index('.')+3 != len(str_amount):
                str_amount += '0'

            str_description = entry['description']

            str_category += '\n'
            if len(str_description) > 23:
                str_category += str_description[0:23] + str_amount.rjust(7)
            else:
                str_category += str_description.ljust(23) + str_amount.rjust(7)

        str_category += f'\nTotal: {self.balance}'
        return str_category

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.income += amount
        self.balance += amount

    def withdraw(self, amount, description=''):
        if self.balance >= amount:
            self.ledger.append({'amount': -amount, 'description': description})
            self.expense += amount
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, destination):
        withdrawed = self.withdraw(amount, f'Transfer to {destination.name}')
        if withdrawed:
            destination.deposit(amount, f'Transfer from {self.name}')
        return withdrawed

    def check_funds(self, amount):
        return amount <= self.balance

def create_spend_chart(categories):
    len_max_name = 0
    expenses = []
    for category in categories:
        expenses.append(category.expense)
        if len_max_name < len(category.name):
            len_max_name = len(category.name)


    str_chart = 'Percentage spent by category'

    total_expense = sum(expenses)
    for y in range(100, -10, -10):
        str_chart += '\n'
        str_chart += str(y).rjust(3) + '| '
        str_chart += ''.join('o  ' if (expense*10//total_expense)*10 >= y else '   ' for expense in expenses )

    str_chart += '\n    -'
    str_chart += ''.join('---' for category in categories)

    names_rjust = [category.name.ljust(len_max_name) for category in categories]
    for i in range(len_max_name):
        str_chart += '\n     '
        str_chart += ''.join(name[i] + '  ' for name in names_rjust)


    print(str_chart)
    return str_chart

food = Category('Food')
food.deposit(1000)

clothing = Category('Clothing')
clothing.deposit(1000)

auto = Category('Auto')
auto.deposit(1000)

food.withdraw(66)
clothing.withdraw(24)
auto.withdraw(10)

create_spend_chart([food, clothing, auto])