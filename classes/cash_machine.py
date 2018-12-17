class BankAccout:


    def __init__(self, account_number, name, password, value, admin):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.value = value
        self.admin = admin

    
accounts_list = [
    BankAccount('0001-1', 'Dinaerte Neto', '123456', 1000, False),
    BankAccount('0001-2', 'Dinaerte Neto', '123456', 1000, False),
    BankAccount('0001-3', 'Dinaerte Neto', '123456', 1000, False),
    BankAccount('0000-0', 'Administrator', '123456', 1000, True),
]