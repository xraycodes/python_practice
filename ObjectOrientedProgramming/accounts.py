import datetime
import pytz

class Account:
    """Simple account with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print(f"Account created for {self.name}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))
    
    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print(f"Amount must be greater than 0 and no more than balance")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.balance}")

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                trans_type = "deposited"
            else:
                trans_type = "withdrawn"
                amount *= -1
            print(f"{amount}, {trans_type}, {date}, {date.astimezone()}")


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.withdraw(500)
    tim.withdraw(2000)

    tim.show_transaction()


