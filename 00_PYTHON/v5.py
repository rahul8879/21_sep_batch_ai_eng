


def load_db():
    db = {
        '123445': {
            'name': 'Alice',
            'age': 20,
            'pwd' : "12345",
        'balance' : 1000
    },
    '123446': {
        'name': 'Bob',
        'age': 22,
        'pwd' : "12346",
        'balance' : 1500
    }
}
    return db


# class Bank:
#     def __init__(self,id):
#         self.__id = id
#         self.__db = load_db()
#     def check_balance(self):
#         if self.__id in self.__db:
#             return self.__db[self.__id]['balance']
#         return None

#     def holiday_list():
#         return ["New Year's Day", "Independence Day", "Thanksgiving", "Christmas"]

#     def add_balance(self,amount):
#         if self.id in self.db:
#             self.db[self.id]['balance'] += amount
#             return self.db[self.id]['balance']
#         return None
    
#     def withdraw_balance(self,amount):
#         if self.id in self.db and self.db[self.id]['balance'] >= amount:
#             self.db[self.id]['balance'] -= amount
#             return self.db[self.id]['balance']
#         return None
    
#     def test_2(self,num):
#         return self.test(num) * 3


# public, private and protected 


class Bank:
    def __init__(self, id):
        self.id = id
        self.db = load_db()

    def check_balance(self):
        if self.id in self.db:
            return self.db[self.id]['balance']
        return None

    def add_balance(self, amount):
        if self.id in self.db:
            self.db[self.id]['balance'] += amount
            return self.db[self.id]['balance']
        return None

    def withdraw_balance(self, amount):
        if self.id in self.db and self.db[self.id]['balance'] >= amount:
            self.db[self.id]['balance'] -= amount
            return self.db[self.id]['balance']
        return None

    def _private_method(self):
        # This is a private method
        return "This is a private method"



class SavingAcc(Bank):
    def __init__(self, id, interest_rate):
        super().__init__(id)
        self.__interest_rate = interest_rate

    def add_interest(self):
        if self.check_balance() is not None:
            interest = self.check_balance() * self.__interest_rate
            self.add_balance(interest)
            return self.check_balance()
        return None

cust_1 = SavingAcc('123445', 0.05)
print(cust_1.add_interest())  # Output: 1000