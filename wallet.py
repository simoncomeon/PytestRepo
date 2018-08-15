
#wallet.py


class InsufficientAmout(Exception):
    pass

class Wallet(object):
    
    def __init__(self, initial_amout=0):
        if not isinstance(initial_amout, int):
            raise TypeError('Please provide Integer'.format(initial_amout))
        self.balance = initial_amout

    def spend_cash(self, amount):
        if not isinstance(amount, int):
            raise TypeError('Please provide Integer'.format(amount))
        if self.balance < amount:
            raise InsufficientAmout('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def  add_cash(self, amount):
        if not isinstance(amount, int):
            raise TypeError('Please provide Integer'.format(amount))
        self.balance += amount
        
    def transfer_reset(self):
        self.balance = 0

    def stock_addition(self, lister):
        if not all(isinstance(n, int) for n in lister):
            raise TypeError('Please proivde Integer'.format(lister))
        self.balance += sum(map(lambda x: x * 2, lister))

















        






        
