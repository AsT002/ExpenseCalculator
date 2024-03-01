class ExpenseCalculator:
    def __init__(self):
        # define & initialize private fields of the class
        self.__expenses = {}
        self.__income = {}
    
    def updateExpense(self, name = "Default", amount = 0):
        # update the expense dictionary with the given name and amount
        self.__expenses[name] = amount
    
    def deleteExpense(self, name =  "Default"):
        # delete the expense with the given name from dictionary
        del self.__expenses[name]
    
    def updateIncome(self, name = "Default", amount = 0):
        # update the income dictionary with the given name and amount
        self.__income[name] = amount 
    
    def deleteIncome(self, name = "Default"):
        # delete the income with the given name from dictionary
        del self.__income[name]
    
    def calculateTotalExpense(self):
        # calculate the total expense from the expense dictionary
        total = 0
        for name in self.__expenses.keys():
            total += self.__expenses[name]
        return total
    
    def calculateTotalIncome(self):
        # calculate the total income from the income dictionary
        total = 0
        for name in self.__income.keys():
            total += self.__income[name]
        return total 
    
    def calculateDifference(self):
        # calculate the difference between total income and total expense
        return self.calculateTotalIncome() - self.calculateTotalExpense()

if (__name__ == "__main__"):
    # create an object of the class
    ec = ExpenseCalculator()
    
    # get expense information from the user
    expense = input("Input an expense name or just \"N\" to stop: ")

    while (expense.lower() != "n"):
        amount = float(input("Input the amount: "))
        ec.updateExpense(expense, amount)
        expense = input("Input an expense or just \"N\" to stop: ")
    
    # get income information from the user
    income = input("Input an income name or just \"N\" to stop: ")

    while (income.lower() != "n"):
        amount = float(input("Input the amount: "))
        ec.updateIncome(income, amount)
        income = input("Input an income or just \"N\" to stop: ")
    
    # print the total expense, total income and difference
    print("Total Expense: ", ec.calculateTotalExpense())
    print("Total Income: ", ec.calculateTotalIncome())
    print("Difference: ", ec.calculateDifference())