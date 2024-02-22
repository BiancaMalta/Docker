class User() :
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show_details(self):
        print("Detalhes Pessoais")
        print("")
        print("Name ", self.name)
        print("Idade ", self.age)
        print("Gênero ", self.gender)

class Bank(User) :
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Saldo disponível foi atualizado : R$", self.balance)
    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Saldo Insufisiente | Saldo disponível : R$ ", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Saldo disponível foi atualizado : R$", self.balance)
    def view_balance(self) :
        self.show_details()
        print("Saldo bancário : R$", self.balance)

