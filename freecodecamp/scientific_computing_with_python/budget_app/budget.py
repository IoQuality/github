import math


class InvalidAmountError(Exception):
    pass


class EmptyLedgerError(Exception):
    pass


class InvalidCategoryError(Exception):
    pass


class Category:

    def __init__(self, category=""):
        self.category = str(category)
        self.ledger = []
        self.category_spending_sum = 0

    def __repr__(self):
        self.get_balance()

    def __str__(self):
        if not self.ledger:
            return f"{self.category.center(30, '*')}\nTotal: 0"
        ledger_string = [self.category.center(30, "*")]
        # finding max length of the monetary value: takes each item, checks its length and find maximum
        monetary_limit = max(len(f"{item['amount']:.2f}") for item in self.ledger)

        # creating left and right sides of the output string, at least one whitespace inbetween
        description_limit = 30 - 1 - monetary_limit
        for item in self.ledger:
            ledger_amount = f"{float(item['amount']):{monetary_limit}.2f}"
            ledger_description = f"{item['description'][0:description_limit]:{description_limit}}"
            ledger_string.append(f"{ledger_description} {ledger_amount}")

        # adding total balance
        ledger_string.append(f"Total: {self.get_balance()}")
        final_string = '\n'.join(ledger_string)
        return final_string

    def deposit(self, amount, description=""):
        # print(f"++ Depositing {amount} to {self.category}")
        try:
            amount = float(amount)
        except ValueError:
            raise InvalidAmountError("ERROR - amount must be a number")
        if amount < 0:
            raise InvalidAmountError("ERROR - amount must be a positive number")

        self.ledger.append({
            "amount": amount,
            "description": str(description)})

    def withdraw(self, amount, description=""):
        try:
            amount = float(amount)
        except ValueError:
            raise InvalidAmountError("ERROR - amount must be an number")
        if amount < 0:
            raise InvalidAmountError("ERROR - amount must be a positive number")

        if self.check_funds(amount):
            self.ledger.append({
                "amount": amount * (-1),
                "description": str(description)})
            self.category_spending_sum = math.fsum([amount])
            return True
        print(f"xx Withdrawing {amount:.2f} from {self.category} not possible - "
              f"not enough funds: {self.get_balance():.2f}")
        return False

    def get_balance(self):
        balance = []
        index_length = len(self.ledger)
        for i in range(index_length):
            balance.append(self.ledger[i]['amount'])
        updated_balance = math.fsum(balance)
        # print(f"!! Getting balance for {self.category}")
        return updated_balance

    def transfer(self, amount, transfer_to_object):
        if not isinstance(transfer_to_object, Category):
            raise InvalidCategoryError(f"ERROR - Cannot transfer {amount} funds from {self.category} "
                                       f"to {transfer_to_object, type(transfer_to_object)}. "
                                       f"The Object is on an instance of the class")
        if not self.check_funds(amount):
            # print("xx Transfer not possible - not enough funds")
            return False
        else:
            self.withdraw(amount, "Transfer to " + transfer_to_object.category)
            # print(f"~~ Transferring {amount} from {self.category} to {transfer_to_object.category}")
            # print(f'||Transfer to {amount} from {self.category}')
            transfer_to_object.deposit(amount, "Transfer from " + self.category)
            # print("  Transfer complete")
            return True

    def check_funds(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            raise InvalidAmountError("ERROR - amount must be a number")
        if amount < 0:
            raise InvalidAmountError("ERROR - amount must be a positive number")

        if amount <= self.get_balance():
            return True
        else:
            return False


################################################
def create_spend_chart(*ledger):
    # total spending sum and per category
    spending_categories = [{"category": i.category, "spending": i.category_spending_sum} for i in ledger[0]]
    total_withdraw_sum = math.fsum([category["spending"] for category in spending_categories])

    # calculating percentages
    if total_withdraw_sum == 0:
        raise ZeroDivisionError("ERROR - Chart can't be generated - there are no withdraws")
    percentages_list = [int(i['spending'] * 100 / total_withdraw_sum) for i in spending_categories]

    # calculating max chart height
    max_category = max(len(category['category']) for category in spending_categories)
    max_chart_height = 10 + max_category + 2

    # generating percentage line
    line_1 = [f"{i:3d}|" for i in range(100, -1, -10)]
    line_1 += [" " * 4] * (max_chart_height - len(line_1))

    # generating inbetween lines
    line_bonus = [' ' for _ in range(11)] + ['-'] + [' ' for _ in range(max_chart_height - 12)]

    # generating a new line list for the end
    line_new_line = [f"\n" for _ in range(max_chart_height)]

    # generating bars for *categories
    generated_lines = {"line_" + str(i + 2): [] for i in range(len(percentages_list))}
    for i in range(len(generated_lines)):
        key = "line_" + str(i + 2)
        generated_lines[key] += [f" " for _ in range(100, percentages_list[i], -10)]
        generated_lines[key] += [f"o" for _ in range(percentages_list[i] + 1, -1, -10)]
        generated_lines[key] += [f"-"]
        generated_lines[key] += [f"{j}" for j in f"{spending_categories[i]['category']}"]
        generated_lines[key] += [f" " for _ in range(max_chart_height - len(generated_lines[key]))]
    # print(generated_lines)

    # creating matrix of list to be transposed
    line_list = [line_1]
    for i in range(len(percentages_list)):
        line_list.append(line_bonus)
        line_list.append(generated_lines["line_" + str(i + 2)])
        line_list.append(line_bonus)
    line_list.append(line_bonus)
    line_list.append(line_new_line)

    # transposing
    matrix = zip(*line_list)
    results = ""
    results += "".join(f"{character}" for line in matrix for character in line)

    # preparing the final string
    final_text = f"Percentage spent by category\n" \
                 f"{results}"
    final_text = final_text[0:-1]
    return f"{final_text}"
