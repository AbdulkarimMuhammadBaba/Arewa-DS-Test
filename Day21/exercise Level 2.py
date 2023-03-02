class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_info(self):
        return "%s %s is person\'s name. his income is ₦%d and his expense is ₦%d." % (
            self.firstname, self.lastname, self.total_income(), self.total_expense())

    def add_income(self, data):
        for k, v in data.items():
            self.incomes[k] = v
        return dict(sorted(self.incomes.items(), key=lambda x: x[1], reverse=True))

    def add_expense(self, data):
        for k, v in data.items():
            self.expenses[k] = v
        return dict(sorted(self.expenses.items(), key=lambda x: x[1], reverse=True))

    def account_balance(self):
        return self.total_income() - self.total_expense()


me = PersonAccount('Abdulkarim', 'Baba', {'Salary': 10000, 'Bonus': 500}, {'Rent': 500, 'General': 200})
print(me.account_info())